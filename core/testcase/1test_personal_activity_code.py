# -*- coding: utf-8 -*-
""" 
@Filename:  core/testcase/test_personal_activity_code
@Author:    小蔡 
@Time:      2023/2/16 18:04
@Describe: ... 
"""
import time

import allure
import pytest
from core.pages import AdminIndexPage
from core.until.data import *


@allure.epic("Web自动化测试平台")
@allure.feature("模块名称：个人活动码测试用例")
@pytest.mark.run(order=4)
class Test_personal_activity_code:
    @allure.title("用例名称：测试创建个人活动码")
    def test_create_code(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_personal_activity_code_page()
        page3 = page2.to_new_personal_activity_code_page()
        msg = page3.create_code(personal_code['personal_code_name'], personal_code['manager_name'],
                                code_all['channel_name'], personal_code['label_name'],
                                personal_code['greeting_nr'])
        assert code_all['assert_msg'] in msg

    @allure.title("用例名称：测试模糊查询个人活动码")
    def test_check_code(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_personal_activity_code_page()
        code_name = f"{personal_code['personal_code_name']}_{personal_code['manager_name']}"
        msg = page2.check_code(code_name)
        assert code_name in msg

    @allure.title("用例名称：测试删除个人活动码")
    def test_delete_code(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_personal_activity_code_page()
        code_name = f"{personal_code['personal_code_name']}_{personal_code['manager_name']}"
        msg = page2.delete_code(code_name)
        assert code_all['delete_prompt'] in msg

