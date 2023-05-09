# -*- coding: utf-8 -*-
"""
@Filename:  core/testcase/test_login.py
@Author:    小蔡 
@Time:      2022/12/1 10:03
@Describe: ... 
"""
import re
import time
from pathlib import Path
import random
from selenium import webdriver
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import autoit
from webdriver_helper import get_webdriver


class Commonshare(object):
    """
    关键字类：用户操作的指令集
    """

    _split_chr = ";;;"

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()  # 创建chrome_options对象
        chrome_options.add_argument('--incognito')
        # chrome_options.add_argument('--headless')   # 无头模式
        driver = get_webdriver(options=chrome_options)
        self.driver = driver
        self.wait = WebDriverWait(
            driver, 10, 0.5
        )
        driver.implicitly_wait(5)
        driver.maximize_window()
        # self.driver = driver
        # self.wait = WebDriverWait(driver, 20)
    # def __init__(self, driver: Chrome):
    #     self.driver = driver
    #     self.wait = WebDriverWait(driver, 10)  # 每次最多等待10秒显式等待

    def get(self, url):
        """
        跳转到指定的页面
        :param url:
        :return:
        """
        # 请求指定url
        self.driver.get(url)

    def sleep(self, x):
        """
        强制等待x秒
        :param x: 等待秒数
        :return:
        """
        time.sleep(x)

    def find_element(self, loc: str):
        """
        元素定位：
        1. 自动等待元素出现
        2. 对定位参数，进行二次处理
        :param number:
        :param loc: 元素定位表达式，格式 "value;;;by"
        定位表达式，支持几个功能：1.可以用json传输基本数据 2. 支持多种定位策略，3. 默认使用XPath
        :return:
        """

        value, *by = loc.split(self._split_chr)  # 1. 从字符串中解析 定位策略
        number = None
        if not by:
            by = By.XPATH  # 如果没有指定定位策略，默认是Xpath
        elif "[" in by[0]:
            number = int(re.findall(rf"{'[0-9]' * (len(by[0]) - 2)}", by[0])[0])
            by = By.XPATH
        else:
            by = getattr(By, by[0])

        def f(dirver):
            if number:
                return self.driver.find_elements(by, value)[number]
            else:
                return self.driver.find_element(by, value)
        element = self.wait.until(f)
        if "app-grid" not in value:
            js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
            # js_sentence_args = "color: red; border: 3px solid red;"
            js_sentence_args = "border: 5px solid red;"
            self.driver.execute_script(js_sentence_light, element, js_sentence_args)
            time.sleep(0.3)
            js_sentence_args = "border: 0px;"
            self.driver.execute_script(js_sentence_light, element, js_sentence_args)

        return element

    def click(self, loc, force=False):
        """
        点击元素，支持强制点击
        :param loc: 定位表达式，支持几个功能：1.可以用json传输基本数据 2. 支持多种定位策略，3. 默认使用XPath
        :param force: 是否强制点击
        :return:
        """
        #  字符串
        element = self.find_element(loc)
        if force:
            # 通过JS代码实现强制点击
            self.driver.execute_script("arguments[0].click()", element)
        else:
            element.click()  # 普通点击

    def input(self, loc, value, force=False):
        """
        在元素中输入内容，支持强制输入
        :param element:  定位到的元素
        :param value:  待输入的内容
        :param force:  是否强制点击
        :return:
        """
        element = self.find_element(loc)
        if force:
            # 通过JS代码实现强制输入
            self.driver.execute_script(f"arguments[0].value='{value}'", element)
        else:
            element.send_keys(value)  # 普通输入

    def clear(self, loc, force=False):
        """
        清空元素内容，支持强制清空
        :param element:  定位到的元素
        :param force:  是否强制点击
        :return:
        """
        element = self.find_element(loc)
        if force:
            # 通过JS代码实现强制输入
            self.driver.execute_script(f"arguments[0].value=''", element)
        else:
            element.clear()  # 普通输入

    def delete(self, loc):
        """
        模拟键盘删除按钮
        """
        element = self.find_element(loc)
        element.send_keys(Keys.DELETE)

    def iframe_enter(self, loc):
        """
        进入指定的框架
        :param element:
        :return:
        """
        element = self.find_element(loc)
        self.driver.switch_to.frame(element)

    def refresh(self):
        self.driver.refresh()

    def quite(self):
        self.driver.quit()

    def iframe_exit(self):
        """
        从框架中退出
        :return:
        """
        self.driver.switch_to.default_content()

    def select(self, loc, text):
        """
        从下拉选择框中，选择指定的选型
        :param element: 下拉选择框的元素
        :param text: 选项显示文本
        :return:
        """
        element = self.find_element(loc)
        Select(element).select_by_visible_text(text)

    def get_text(self, loc):
        el = self.element = self.find_element(loc)
        return el.text

    def upload(self, loc, file):
        """
        在指定元素中生成文件
        :param element: 元素
        :param file: 文件的路径 （支持相对路径）
        :return:
        """

        element = self.find_element(loc)
        path = Path(file)  # path对象
        path.absolute()  # 转为绝对路径

        element.send_keys(str(path.absolute()))  # 必须转字符串

    def read1(self):
        with open('../../Business/圣墟.txt', 'r', encoding='utf-8') as files:
            str1 = files.read()
            return str1

    # 获取数据源2
    def read2(self):
        with open("../../Business/苍穹战纪.txt", 'r', encoding='utf-8') as files:
            str2 = files.read()
            return str2

    """""
        发送文字方法：
        number:发送次数
        s_input:发送输入框路径
        s_btn:发送按钮
    """""

    def s_Text(self, number, s_input, s_btn):
        for c in range(1, number + 1, 1):
            # 函数生成随机发送消息内容长度
            math = random.randint(1, 30)
            # 随机生成字符
            nr = [random.choice(self.read1() + self.read2()) for i in range(math)]
            nr = ",".join(nr)
            nr = nr.replace('\n', '')
            nr = nr.replace(',', '')
            nr = f"{nr}，<<第{c}条消息>>"
            self.input(s_input, nr)
            self.click(s_btn)
            print(f"第{c}条消息已发送，发送内容为({nr}),发送内容长度为{math}")
            if c == number:
                self.input(s_input, f"发送完毕，已发送{c}条消息")
                print(f"发送完毕，已发送{c}条消息")
                self.click(s_btn)

    """""
        发送视频方法：
        number:发送次数
        s_cp:插入图片路径
        s_input:发送输入框路径
        s_btn:发送按钮路径
    """""

    def s_Picture(self, number, s_cp, s_input, s_btn):
        for c in range(1, number + 1, 1):
            # 单击插入图片按钮
            self.click(s_cp)
            time.sleep(3)
            # 聚焦
            WebDriverWait(self.driver, 50).until(
                lambda x: autoit.control_focus("打开", "[CLASS:Button; INSTANCE:1]"))
            time.sleep(1)
            # 输入文本
            path = ('C:\\Users\\wangy\\Desktop\\1.jpg')
            autoit.control_set_text("打开", "[CLASS:Edit; INSTANCE:1]", path)
            time.sleep(1)
            # 单击打开按钮
            autoit.control_click("打开", "[CLASS:Button; INSTANCE:1]")
            time.sleep(1)
            self.click(s_btn)
            print(f"第{c}张图片已发送")
            if c == number:
                self.input(s_input, f"发送完毕，已发送{c}张图片")
                print(f"发送完毕，已发送{c}张图片")
                self.click(s_btn)
                time.sleep(5)

    """""
        发送视频方法：
        number:发送次数
        s_cv:插入视频路径
        s_input:发送输入框路径
        s_btn:发送按钮路径
    """""

    def s_Viode(self, number, s_cv, s_input, s_btn):
        for c in range(1, number + 1, 1):
            # 单击插入视频按钮
            self.click(s_cv)
            time.sleep(3)
            # 聚焦
            WebDriverWait(self.driver, 50).until(
                lambda x: autoit.control_focus("打开", "[CLASS:Button; INSTANCE:1]"))
            time.sleep(1)
            path = ('E:\\公司篇\\广州趣渔科技有限公司上海分公司\\图库\\视频\\测试视频.mp4')
            # 输入文本
            autoit.control_set_text("打开", "[CLASS:Edit; INSTANCE:1]", path)
            time.sleep(1)
            # 单击打开按钮
            autoit.control_click("打开", "[CLASS:Button; INSTANCE:1]")
            time.sleep(1)
            self.click(s_btn)
            print(f"第{c}个视频已发送")
            if c == number:
                self.input(s_input, f"发送完毕，已发送{c}个视频")
                print(f"发送完毕，已发送{c}个视频")
                self.click(s_btn)
                time.sleep(5)

    """""
        发送表情方法：
        number:发送次数
        s_cv:插入视频路径
        s_input:发送输入框路径
        s_btn:发送按钮路径
    """""

    def s_Emojis(self, number, s_cv, s_input, s_btn):
        for c in range(1, number + 1, 1):
            # 单击插入图片按钮
            self.click(s_cv)
            # 聚焦
            autoit.control_focus("打开", "[CLASS:Button; INSTANCE:1]")
            time.sleep(1)
            path = ('E:\\公司篇\\广州趣渔科技有限公司上海分公司\\图库\\视频\\测试视频.mp4')
            # 输入文本
            autoit.control_set_text("打开", "[CLASS:Edit; INSTANCE:1]", path)
            time.sleep(1)
            # 单击打开按钮
            autoit.control_click("打开", "[CLASS:Button; INSTANCE:1]")
            time.sleep(1)
            self.click(s_btn)
            print(f"第{c}个视频已发送")
            if c == number:
                self.input(s_input, f"发送完毕，已发送{c}张图片")
                print(f"发送完毕，已发送{c}张图片")
                self.click(s_btn)
                time.sleep(5)
