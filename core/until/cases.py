# -*- coding: utf-8 -*-
""" 
@Filename:  core/until/case
@Author:    小蔡 
@Time:      2023/2/24 11:16
@Describe: ... 
"""


import logging
import time
import unittest

import allure
import ddt
import pytest

from core.until.kdt import KeyWord

logger = logging.getLogger(__name__)


def handle_name(s):
    try:
        l = s.index("(")
        r = s.index(")")

        case_name = s[:l]  # 用例名称
        fixture_name = s[l + 1 : r]  # 夹具名称

        return case_name, fixture_name
    except:
        logger.warning(f"解析fixture出错: {s}", exc_info=True)
        return s, "driver"


def handle_step(s):
    name = s[1]
    key = s[2]
    args = []
    for arg in s[3:]:
        if arg is not None:
            args.append(arg)

    return name, key, args


def create_unitest_by_excel(suite_list):
    Test_list = []  # 列表中的测试用不会被pytest识别

    for case in suite_list:  # 列表中读取每一个工作表

        @ddt.ddt
        class TestA(unittest.TestCase):
            @ddt.data(*case["case_list"])  # 每一个工作表，读取每一个用例
            def test_a(self, case):
                print(case)

        Test_list.append(TestA)

    return Test_list


def create_pytest_case(suite_list):
    # suite 每一个Excel中sheet表示一个套件，里面会包含多个用例

    test_list = []

    for suite in suite_list:  # 遍历 suite

        @allure.feature("Web自动化测试平台")
        @allure.story(suite["name"])
        @pytest.mark.parametrize(
            "case",
            suite["case_list"],
            ids=[
                handle_name(case["name"])[0] for case in suite["case_list"]
            ],  # 参数化测试的名字
        )  # 参数化的本质：动态生成用例
        def test_abc(case, request):
            logger.info("测试用例开始执行")
            # print(data)

            # 如果能够调用夹具，那么就有了浏览
            # 根据excel内容，动态调用指定的夹具
            # 1. 拿到用例名称     用例4(admin_driver)
            # 2. 从用例名称中，解析夹具名称    admin_driver
            case_name = handle_name(case["name"])[0]
            fixture_name = handle_name(case["name"])[1]

            logger.info(f"解析用例名称:{case_name=}, {fixture_name=}")

            driver = request.getfixturevalue(fixture_name)
            kw = KeyWord(driver)
            kw.iframe_exit()
            if "码" in case_name:
                kw.click("/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[4]/div/span")
            kw.refresh()
            # 根据excel内容进行关键字的调用
            for step in case["steps"]:
                name, key, args = handle_step(step)  # 这三个变量，可以再进行处理、修改
                # 能不能加载csv文件
                # 能行循环调用 func
                logger.info(f"执行关键字{name=}, {key=}, {args=}")

                with allure.step(name):  # 在allure显式测试步骤
                    func = getattr(kw, key)  # 通过反射，难道关键字执行函数
                    func(*args)  # 调用关键字函数

                # allure.attach(driver.get_screenshot_as_png(), name)  #截图
            logger.info("测试用例执行结束")
            time.sleep(0.5)     # 硬件条件勉强支持脚本运行，不时会影响元素定位，故此处设置每个用例执行结束后等待一段时间
        test_list.append(test_abc)  # 函数加入到列表

    return test_list  # 返回列表，列表可能有多个用例
