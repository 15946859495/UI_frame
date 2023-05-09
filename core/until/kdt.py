"""
@Filename:  core/testcase/test_login.py
@Author:    小蔡
@Time:      2022/09/28 20:30
@Describe: ...
"""
import re
import time
from shutil import rmtree

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from selenium.webdriver.common.actions.pointer_input import PointerInput
from pathlib import Path
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_helper import debugger, get_webdriver, logger
import autoit
from core.until.open_tool import check_download_file, clear_download_file, read_excel
from selenium.webdriver.chrome.options import Options
from core.until.settings import settings

vars = {}  # 关键字的变量


class KeyWord:
    """
    关键字类：用户操作的指令集
    """

    _split_chr = ";;;"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, settings["wait_max"], settings["wait_poll"]
        )  # 每次最多等待10秒显式等待
        # 窗口最大化
        self.driver.maximize_window()

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

    def keyboard_enter(self, loc):
        element = self.find_element(loc)
        element.send_keys(Keys.ENTER)

    def input(self, loc, value="", force=False):
        """
        在元素中输入内容，支持强制输入
        :param element:  定位到的元素
        :param value:  待输入的内容
        :param force:  是否强制点击
        :return:
        """
        element = self.find_element(loc)
        # js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
        # js_sentence_args = "color: red; border: 3px solid yellow;"
        # self.driver.execute_script(js_sentence_light, element, js_sentence_args)
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

    def quite(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

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

        el = self.find_element(loc)

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

    def assert_text(self, loc, text):
        """
        断言：页面中的文本，符合预期
        :param loc:
        :param text:
        :return:
        """
        self.sleep(0.5)
        element = self.find_element(loc)
        js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
        js_sentence_args = "border: 5px solid red;"
        self.driver.execute_script(js_sentence_light, element, js_sentence_args)
        logger.info(f"assert ({text=}) == ({element.text=})")
        allure.attach(self.driver.get_screenshot_as_png(), "断言截图")
        assert text == element.text

    def assert_text_in(self, loc, text):
        """
        断言：文本是否在定位元素中
        :param loc:
        :param text:
        :return:
        """
        self.sleep(0.5)
        element = self.find_element(loc)
        js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
        js_sentence_args = "border: 5px solid red;"
        self.driver.execute_script(js_sentence_light, element, js_sentence_args)
        logger.info(f"assert ({text=}) in ({element.text=})")
        allure.attach(self.driver.get_screenshot_as_png(), "断言截图")
        assert text in element.text

    def assert_mandatory_field(self, text: str):
        """
        断言：列表内容是否在页面源码中
        :param loc:
        :param text:
        :return:
        """
        self.sleep(0.5)
        msg = self.driver.page_source

        allure.attach(self.driver.get_screenshot_as_png(), "断言截图")
        text = text.replace(' ', '').split(',')
        logger.info(f"({text})")
        for i in text:
            logger.info(f"assert ({i=}) in ({msg=})")
            assert i in msg

    def assert_mandatory_field_no(self, text: str):
        """
        断言：列表内容是否在页面源码中
        :param loc:
        :param text:
        :return:
        """
        self.sleep(0.5)
        msg = self.driver.page_source

        allure.attach(self.driver.get_screenshot_as_png(), "断言截图")
        text = text.replace(' ', '').split(',')
        logger.info(f"({text})")
        for i in text:
            logger.info(f"assert ({i=}) not in ({msg=})")
            assert i not in msg

    def assert_text_in_list(self, loc, text):
        """
        断言：文本在列表中
        :param loc:
        :param text:
        :return:
        """
        self.sleep(0.5)
        element = self.find_element(loc)
        js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
        js_sentence_args = "border: 5px solid red;"
        self.driver.execute_script(js_sentence_light, element, js_sentence_args)
        msg = element.text.split('\n')
        text = text.replace(' ', '').split(',')
        logger.info(f"assert ({text=}) in ({msg=})")
        allure.attach(self.driver.get_screenshot_as_png(), "断言截图")
        for i in text:
            logger.info(f"assert ({i=}) in ({msg=})")
            assert i in msg

    def assert_list_in(self, loc, text):
        """
        断言：列表内容是否在定位元素中
        :param loc:
        :param text:
        :return:
        """
        self.sleep(0.5)
        element = self.find_element(loc)
        allure.attach(self.driver.get_screenshot_as_png(), "断言截图")
        text = text.replace(' ', '').split(',')
        logger.info(f"assert ({text=}) in ({element.text=})")
        for i in text:
            logger.info(f"assert ({i=}) in ({element.text=})")
            assert i in element.text

    def clear_file(self, text):
        text = text.replace(' ', '').split(',')
        logger.info(f"({text})")
        if check_download_file(text[0], text[1], text[2]):
            clear_download_file(text[0], text[1])

    def assert_file(self, text):
        """
        断言：导出excel文件及其表头
        :param loc:
        :param text:
        :return:
        """
        text = text.replace(' ', '').split(',')
        status = check_download_file(text[0], text[1], text[2])
        if status:
            msg = read_excel(text[0] + "\\" + text[1])
            for i in text[3::]:
                logger.info(f"assert ({i=}) in ({msg=})")
                assert i in msg
        else:
            return False

    def ddt_csv(self, loc, file):
        # 打开csv文件，读取数据，返回
        # return [1,2,3]
        value = 123
        self.input(loc, value)

    def save_text(self, loc, var_name):
        """
        将元素的text属性保存到变量中
        :param loc: 元素的定位表达式
        :param var_name:  变量名
        :return:
        """
        element = self.find_element(loc)
        text = element.text  # 获取元素的text属性
        vars[str(var_name)] = text

    def input_var(self, loc, var_name):
        """
        将变量中的内容，输入到元素
        :param loc:
        :param var_name:
        :return:
        """
        var = vars.get(var_name, "")  # 读取变量

        return self.input(loc, var)  # 使用之前的关键字完成输入

    def long_touch(self, loc):
        element = self.find_element(loc)
        # 通过AC来实现 长按效果

        ac = ActionChains(self.driver)

        ac.move_to_element(element)  # 移动到元素上
        ac.w3c_actions.pointer_action.pointer_down()  # 按下
        ac.w3c_actions.pointer_action.pause(1)  # 暂停一秒
        ac.w3c_actions.pointer_action.release()  # 抬起

        ac.perform()  # 执行动作

    def swipe(self, x1, y1, x2, y2):
        # 从(x1,y1) 滑动到 （x2,y2）

        ac = ActionChains(self.driver)
        action = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )

        ac.w3c_actions = action  # 将mouse 替换为 touch

        ac.w3c_actions.pointer_action.move_to_location(x1, y1)
        ac.w3c_actions.pointer_action.pointer_down()  # 按下
        ac.w3c_actions.pointer_action.pause(0.5)  # 暂停0.5秒以下
        ac.w3c_actions.pointer_action.move_to_location(x2, y2)
        ac.w3c_actions.pointer_action.release()  # 抬起

        print(time.time())
        ac.perform()  # 执行动作

        print(time.time())

    def new_touch(self, x, y):
        self.ac = ActionChains(self.driver)
        action = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )

        self.ac.w3c_actions = action  # 将mouse 替换为 touch
        self.ac.w3c_actions.pointer_action.move_to_location(x, y)
        self.ac.w3c_actions.pointer_action.pointer_down()  # 按下

    def swipe_touch(self, x, y):

        self.ac.w3c_actions.pointer_action.pause(0)  #
        self.ac.w3c_actions.pointer_action.move_to_location(x, y)

    def perform_touch(self):
        print(time.time())
        self.ac.w3c_actions.pointer_action.release()  # 抬起
        self.ac.perform()  # 执行动作
        self.ac = None
        print(time.time())

    def new_ac(self):
        self.ac = ActionChains(self.driver)
        self.p_count = 0  # 指针数量

    def new_click(self, loc):  # 创造新的，而不是覆盖旧的
        """多指点击"""

        self.p_count += 1  # 每次添加新的指针，计数器都会变化

        p = self.ac.w3c_actions.add_pointer_input(
            "touch", f"p_{self.p_count}"
        )  # 为这个指针创建独一无二的名字

        p_action = PointerActions(p)

        # 1. 定位元素
        element = self.find_element(loc)
        # 2. 移动指针到元素上面
        p_action.move_to(element)
        # 3.  点击 = 按下 + 抬起
        #  只按下 不抬起
        p_action.pointer_down()

    def perform_click(self):
        self.ac.perform()
        self.p_count = 0  # 指针数量

    def activity(self, package_name, activity_name):
        self.driver.start_activity(package_name, activity_name)

    def htt_user_id(self):

        path = Path("D:\\http_logs\\")

        rmtree(path)  # 删除内容

        time.sleep(5)

        for _path in path.glob("**/request.txt"):
            # print(_path)
            content = _path.read_text()
            if "user_id" in content:
                line = content.split("\n")[0]
                line = line.replace(" HTTP/1.1", "")
                index = line.find("user_id=")
                var = line[index + len("user_id="):]

                return var

    def read1(self):
        with open('圣墟.txt', 'r', encoding='utf-8') as files:
            str1 = files.read()
            return str1

    # 获取数据源2
    def read2(self):
        with open("苍穹战纪.txt", 'r', encoding='utf-8') as files:
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
