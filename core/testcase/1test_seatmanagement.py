# -*- coding: utf-8 -*-
""" 
@Filename:  core/testcase/test_seatmanagement
@Author:    小蔡 
@Time:      2023/2/7 17:51
@Describe: ... 
"""
import time
import allure
import pytest
from core.pages import AdminIndexPage
from core.until.data import *


@allure.epic("Web自动化测试平台")
@allure.feature("模块名称：席位管理测试用例")
@pytest.mark.run(order=3)
class Test_SeatManagement:
    @allure.title("用例名称：测试席位管理主页列表导出功能")
    def test_export_seat(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_seat_management_page()
        msg = page2.export_seat(Seat_data['exportPath'], Seat_data["exportSeat"], load=3)
        for i in Seat_data['exportcheck']:
            assert i in msg
