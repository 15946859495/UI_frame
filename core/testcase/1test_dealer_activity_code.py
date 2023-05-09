# -*- coding: utf-8 -*-
""" 
@Filename:  core/testcase/test_dear_code
@Author:    小蔡 
@Time:      2023/2/23 18:40
@Describe: ... 
"""
import allure
import pytest
from core.pages import AdminIndexPage
from core.until.data import *


@allure.epic("Web自动化测试平台")
@allure.feature("模块名称：门店活动码测试用例")
@pytest.mark.run(order=5)
class Test_dealer_activity_code:
    @allure.title("用例名称：测试创建门店活动码")
    def test_create_cod(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_dealer_activity_code_page()
        page3 = page2.to_new_dealer_activity_code_page()
        msg = page3.create_code(dealer_code['dealer_code_name'], dealer_code['manager_name'],
                                code_all['channel_name'], dealer_code['label_name'],
                                dealer_code['greeting_nr'])
        assert code_all['assert_msg'] in msg
