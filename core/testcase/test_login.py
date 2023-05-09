# -*- coding: utf-8 -*-
"""
@Filename:  core/testcase/test_login.py
@Author:    小蔡 
@Time:      2022/09/28 20:30 
@Describe: ... 
"""

import csv
import pytest
import allure
from core.pages import IndexPage
from core.until.data import *


@allure.epic("Web自动化测试平台")
@allure.feature("模块名称：用户登录测试用例")
@pytest.mark.run(order=1)
class Test_Login:
    url = 'https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr'
    @pytest.mark.parametrize(
        "data",
        csv.DictReader(open('data/ddt_login.csv', encoding="utf-8-sig"))
    )
    @allure.title("用例名称：验证用户名或密码为空时登录")
    def test_login(self, driver, data):
        page = IndexPage(driver)
        msg = page.login(data["用户名"], data["密码"], self.url)
        assert msg == data["登录结果"]

    @allure.title("用例名称：验证用户名正确，密码错误时登录")
    def test_incorrect_password(self, driver):
        page = IndexPage(driver)
        msg = page.login_incorrect_password("19542812247", "9444994", self.url)
        assert msg in login_data["Incorrect_Password"]

    @allure.title("用例名称：验证用户名错误，密码正确时登录")
    def test_account_error(self, driver):
        page = IndexPage(driver)
        msg = page.login_incorrect_password("19542812246", "LEdiiUpV", self.url)
        assert msg in login_data["Incorrect_Password"]

    @allure.title("用例名称：验证用户名错误，密码错误时登录")
    def test_all_error(self, driver):
        page = IndexPage(driver)
        msg = page.login_incorrect_password("19542812246", "LEdiiUp", self.url)
        assert msg in login_data["Incorrect_Password"]

    @allure.title("用例名称：验证用户正常登录")
    def test_normal_login(self, driver):
        page = IndexPage(driver)
        msg = page.login_normal_login("19542812247", "LEdiiUpV", self.url)
        assert msg == login_data["Normal_Login"]
