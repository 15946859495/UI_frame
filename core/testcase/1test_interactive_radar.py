# -*- coding: utf-8 -*-
"""
@Filename:  core/testcase/test_login.py
@Author:    小蔡 
@Time:      2022/12/5 15:19
@Describe: ... 
"""
import time

import allure
import pytest

from core.pages import AdminIndexPage
from core.until.data import *


@allure.epic("Web自动化测试平台")
@allure.feature("模块名称：互动雷达测试用例")
@pytest.mark.run(order=2)
class Test_Radar:
    @allure.title("用例名称：测试正常创建互动雷达")
    def test_create_radar(self, admin_driver):
        time.sleep(1)
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        page3 = page2.to_new_radar_page()
        msg = page3.create_radar(Radar_data['Radar_title'], Radar_data['Radar_link'], Radar_data['Link_title'],
                                 Radar_data['Link_summary'])
        assert Radar_data['test_CreateRadar_check'] in msg

    @allure.title("用例名称：测试雷达名称重复创建互动雷达")
    def test_create_radar_samename(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        page3 = page2.to_new_radar_page()
        msg = page3.create_radar(Radar_data['Radar_title'], Radar_data['Radar_link'], Radar_data['Link_title'],
                                 Radar_data['Link_summary'])
        assert Radar_data['test_CreateRadar_samename_check'] in msg

    @allure.title("用例名称：测试创建互动雷达必填项为空")
    def test_create_radar_mandatory_field(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        page3 = page2.to_new_radar_page()
        msg = page3.create_radar("", "", "", "", "1")
        for ts in Radar_data['test_CreateRadar_Mandatoryfield_check']:
            assert ts in msg

    @allure.title("用例名称：测试互动雷达重置查询功能")
    def test_check_radar(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        msg = page2.check_radar(Radar_data['title_reset'], Radar_data['creater_reset'], Radar_data['title'],
                                Radar_data['creater'])
        assert Radar_data['title'] == msg

    @allure.title("用例名称：测试互动雷达删除功能")
    def test_delete_radar(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        msg = page2.delete_radar(Radar_data['title'], Radar_data['creater'])
        assert Radar_data['test_deleteRadar_check'] == msg

    @allure.title("用例名称：测试互动雷达主页列表导出功能")
    def test_export_radar(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        msg = page2.export_radar(Radar_data['exportPath'], Radar_data["exportRadar"], load=3)
        for i in Radar_data['exportcheck']:
            assert i in msg

    @allure.title("用例名称：测试互动雷达主页列表字段完整性")
    def test_check_radar_field(self, admin_driver):
        page = AdminIndexPage(admin_driver)
        page2 = page.to_admin_radar_page()
        msg = page2.check_radar_field()
        for i in Radar_data["checkRadarnr"]:
            assert i in msg
