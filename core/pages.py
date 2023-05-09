# -*- coding: utf-8 -*-
import time

from selenium.webdriver import Keys

from core.until.kdt import KeyWord
from core.until.funcs import is_login
from core.until.open_tool import check_download_file, clear_download_file, read_excel
from core.until.element import *


class BasePage(KeyWord):
    """抽象化类，包含所有页面共用代码"""


class IndexPage(BasePage):
    """首页（登录）页面"""
    user = '//input[@placeholder="请输入手机号"]'  # 用户名输入框
    password = '//input[@placeholder="请输入密码"]'  # 密码输入框
    msg = "/html/body/div/div/div/div/div/div/div[2]/form/div[1]/span[2]"   # 输入框上提示信息
    msg2 = "/html/body/div[2]/div/div[1]/div/div[2]"    # 弹窗提示信息
    msg3 = "//label[contains(text(),'神秘人')]"    # 首页昵称
    btn_login = "button;;;TAG_NAME"  # 登录按钮

    def login(self, username, password, url):
        """必填项为空登录"""
        self.get(url)
        # 输入账号
        self.clear(self.user)
        self.input(self.user, username)
        # 输入密码
        self.clear(self.password)
        self.input(self.password, password)
        # 点击登录按钮
        self.click(self.btn_login)
        # 获取提示信息
        msg = self.get_text(self.msg)
        return msg

    def login_incorrect_password(self, username, password, url):
        """账号或密码错误登录"""
        # 输入账号
        self.get(url)
        self.clear(self.user)

        self.input(self.user, username)
        # 输入密码
        self.clear(self.password)

        self.input(self.password, password)
        # 点击登录按钮
        self.click(self.btn_login)
        # 获取提示信息
        msg = self.get_text(self.msg2)
        return msg

    def login_normal_login(self, username, password, url):
        """正常登录"""
        self.get(url)
        # 输入账号
        self.clear(self.user)
        self.input(self.user, username)
        # 输入密码
        self.clear(self.password)
        self.input(self.password, password)
        # 点击登录按钮
        self.click(self.btn_login)
        # 获取提示信息
        msg = self.get_text(self.msg3)
        time.sleep(3)
        return msg

    def admin_login(self, username, password, url):
        self.get(url)
        # 输入账号
        self.clear(self.user)
        self.input(self.user, username)
        # 输入密码
        self.clear(self.password)
        self.input(self.password, password)
        # 点击登录按钮
        self.click(self.btn_login)
        self.sleep(1)
        return is_login(self.driver)  # 使用 is_login函数返回值作为交互返回值


class AdminIndexPage(BasePage):
    """首页页面"""
    enter_radar = '/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[4]/div/span'    # 导航栏互动雷达选项
    enter_management = "/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[11]/div/div/span"  # 导航栏管理
    enter_qd_code = "//span[contains(text(),'渠道活码工具')]"  # 导航栏渠道活码工具选项
    enter_active_code = "//span[contains(text(),'活动码')]"    # 导航栏活动码选项
    enter_personal_code = "//span[contains(text(),'个人活动码')]"  # 导航栏个人活动码选项
    enter_seat_page = '//span[contains(text(),"席位管理")]'  # 导航栏席位管理选项
    enter_dealer_code = "//span[contains(text(),'门店活动码')]"  # 导航栏门店活动码选项

    def to_admin_radar_page(self):
        """进入互动雷达页面"""
        self.click(self.enter_radar)
        self.sleep(2)
        self.driver.refresh()
        self.sleep(2)
        return AdminRadarPage(self.driver)

    def to_seat_management_page(self):
        """进入席位管理页面"""
        self.click(self.enter_management)
        self.click(self.enter_seat_page)
        self.driver.refresh()
        return AdminSeatManagementPage(self.driver)

    def to_personal_activity_code_page(self):
        """进入个人活动码页面"""
        msg = self.get_text('//div[@class = "app-layout-nav-wrap-in"]')
        if "个人活动码" in msg:
            self.click(self.enter_qd_code)
        self.click(self.enter_qd_code)
        self.click(self.enter_active_code)
        self.click(self.enter_personal_code)
        return AdminPersonalActivityCodePage(self.driver)

    def to_dealer_activity_code_page(self):
        """进入门店活动码页面"""
        msg = self.get_text('//div[@class = "app-layout-nav-wrap-in"]')
        if "个人活动码" in msg:
            self.click(self.enter_qd_code)
        self.click(self.enter_qd_code)
        self.click(self.enter_active_code)
        self.click(self.enter_dealer_code)
        return AdminDealerActivityCodePage(self.driver)


class AdminSeatManagementPage(BasePage):
    """席位管理页面"""
    sm_export_button = '//span[contains(text(),"导出")]'  # 席位管理主页列表导出按钮

    def export_seat(self, file_path, file_name, load):
        """导出席位管理列表"""
        self.iframe_enter(iframe_enter_seat)
        if check_download_file(file_path, file_name, load):
            clear_download_file(file_path, file_name)
        self.click(self.sm_export_button)
        self.iframe_exit()
        status = check_download_file(file_path, file_name, load)
        msg = ""
        if status:
            msg = read_excel(file_path + "\\" + file_name)
        return msg


class AdminRadarPage(BasePage):
    """互动雷达主页"""
    Radar_title_check_input_box = '//label[contains(text(),"雷达标题")]/../div/div/input'  # 雷达标题查询输入框
    Radar_creater_check_input_box = '//label[contains(text(),"创建人")]/../div/div/input'  # 雷达创建人查询输入框
    check_button = '//span[contains(text(),"查询")]'  # 查询按钮
    reset_button = '//span[contains(text(),"重置")]'  # 重置按钮
    delete_button = '//tbody[1]/tr/td[1]/div/div/span[4]'  # 删除按钮
    delete_check_button = '//div[@class="ivu-modal-confirm-footer"]/button[2]'  # 删除确认按钮
    delete_popover = '//div[@class="ivu-notice-title"]'  # 删除提示弹窗
    export_button = '//span[contains(text(),"导出Excel")]'    # 导出Excel按钮
    channelmanagement_button = "//span[contains(text(),'渠道管理')]"  # 渠道管理按钮
    createradar_button = "//span[contains(text(),'创建雷达')]"  # 创建雷达按钮
    radar_field2 = '//tbody[1]/tr/td[2]/div/div'  # 互动雷达主页列表第二行
    radar_field1 = "//table/thead[1]/tr"  # 互动雷达主页列表第一行

    def to_new_radar_page(self):
        """去创建雷达页面"""
        self.iframe_enter(iframe_enter_radar)
        self.click(self.createradar_button)  # 点击创建雷达按钮
        self.iframe_exit()
        self.sleep(1)
        self.driver.refresh()
        self.sleep(2)
        return AdminNewRadarPage(self.driver)

    def to_radar_data_page(self):
        """去雷达数据页面"""
        pass

    def check_radar(self, title_reset, creater_reset, title, creater):
        """测试查询互动雷达"""
        time.sleep(3)
        self.refresh()
        self.iframe_enter(iframe_enter_radar)
        self.input(self.Radar_title_check_input_box, title_reset)
        self.input(self.Radar_creater_check_input_box, creater_reset)
        self.click(self.check_button)
        self.click(self.reset_button)
        time.sleep(3)
        self.input(self.Radar_title_check_input_box, title)
        self.input(self.Radar_creater_check_input_box, creater)
        self.click(self.check_button)
        msg = self.get_text(self.radar_field2)
        self.sleep(1)
        self.iframe_exit()
        self.sleep(2)
        return msg

    def delete_radar(self, title, creator):
        """测试删除互动雷达"""
        time.sleep(3)
        self.refresh()
        self.iframe_enter(iframe_enter_radar)
        self.input(self.Radar_title_check_input_box, title)  # 输入雷达标题
        self.input(self.Radar_creater_check_input_box, creator)  # 输入雷达创建人用户名
        self.click(self.check_button)  # 点击查询按钮
        self.sleep(1)
        self.click(self.delete_button)  # 点击删除按钮
        self.iframe_exit()
        self.click(self.delete_check_button)  # 点击删除确认按钮
        msg = self.get_text(self.delete_popover)  # 获取删除后提示信息
        self.sleep(2)
        return msg

    def export_radar(self, file_path, file_name, load):
        """测试导出互动雷达"""
        self.iframe_enter(iframe_enter_radar)
        if check_download_file(file_path, file_name, load):
            clear_download_file(file_path, file_name)
        self.click(self.export_button)
        self.iframe_exit()
        status = check_download_file(file_path, file_name, load)
        msg = ""
        if status:
            msg = read_excel(file_path + "\\" + file_name)
        return msg

    def check_radar_field(self):
        """测试互动雷达主页列表字段完整性"""
        self.iframe_enter(iframe_enter_radar)
        msg = self.get_text(self.radar_field1)
        self.iframe_exit()
        return msg


class AdminNewRadarPage(BasePage):
    """创建互动雷达页面"""
    Radar_title_input_box = '//input[@placeholder="请输入雷达标题"]'  # 雷达标题输入框
    Radar_link_input_box = '//input[@placeholder="请输入雷达链接"]'  # 雷达链接输入框
    Link_title_input_box = '//input[@placeholder="请输入链接标题"]'  # 链接标题输入框
    Link_summary_input_box = '//textarea[@placeholder="请输入链接摘要"]'  # 链接摘要输入框
    Select_cover_button = '//button[contains(text(),"选择封面")]'  # 选择封面按钮
    img = '//div[@class = "app-grid-flex"]/div[1]/div/div[1]/img'  # 图片
    img_check_box = '//div[@class = "app-grid-flex"]/div[1]/div/div[2]/label/span/input'  # 图片复选框
    Confirm_button = '//span[contains(text(),"确定")]'  # 选择图片确认按钮
    Create_confirm_button = '//span[contains(text(),"确定")]'  # 创建雷达确认按钮
    Create_popover = '//div[@class = "ivu-notice-notice-content"]/div'  # 创建提示弹窗

    def create_radar(self, radar_title, radar_link, link_title, link_summary, input_text=None):
        """测试创建互动雷达"""
        self.iframe_enter(iframe_create_radar)
        self.input(self.Radar_title_input_box, radar_title)  # 输入雷达标题
        self.input(self.Radar_link_input_box, radar_link)  # 输入雷达链接
        self.input(self.Link_title_input_box, link_title)  # 输入链接标题
        self.input(self.Link_summary_input_box, link_summary)  # 输入链接摘要
        if input_text is None:
            self.click(self.Select_cover_button)  # 点击选择封面按钮
            self.iframe_exit()
            self.click(self.img)  # 点击图片
            self.click(self.img_check_box)  # 点击图片复选框
            self.click(self.Confirm_button)  # 点击选择图片确认按钮
            self.iframe_enter(iframe_create_radar)
            self.click(self.Create_confirm_button)  # 点击创建雷达确认按钮
            self.iframe_exit()
            msg = self.get_text(self.Create_popover)
        else:
            self.click(self.Create_confirm_button)  # 点击创建雷达确认按钮
            msg = self.driver.page_source
            self.iframe_exit()
        self.sleep(2)
        return msg


class AdminPersonalActivityCodePage(BasePage):
    """个人活动码页面"""
    btn_createcode = "//span[contains(text(),'创建个人活动码')]"
    input_codename = '//label[contains(text(),"活码名称")]/../div/div/input'
    btn_check = '//span[contains(text(),"查询")]'
    btn_delete = '//tbody[1]/tr/td[1]/div/div/span[3]'
    code_field2 = '//tbody[1]/tr/td[3]/div'
    btn_delete_check = '//span[contains(text(),"确定")]'
    popover_delete = '//div[@class="ivu-notice-title"]'

    def to_new_personal_activity_code_page(self):
        """进入新增个人活动码页面"""
        self.iframe_enter(iframe_enter_personalActivityCode)
        self.click(self.btn_createcode)
        self.iframe_exit()
        self.sleep(3)
        return AdminNewPersonalActivityCodePage(self.driver)

    def check_code(self, code_name):
        """查询个人活动码"""
        self.refresh()
        self.iframe_enter(iframe_enter_personalActivityCode)
        self.input(self.input_codename, code_name)
        self.click(self.btn_check)
        msg = self.get_text(self.code_field2)
        self.iframe_exit()
        return msg

    def delete_code(self, code_name):
        """删除个人活动码"""
        self.refresh()
        self.iframe_enter(iframe_enter_personalActivityCode)
        self.input(self.input_codename, code_name)
        self.click(self.btn_check)
        time.sleep(1)
        self.click(self.btn_delete)
        self.iframe_exit()
        self.click(self.btn_delete_check)
        msg = self.get_text(self.popover_delete)
        self.iframe_exit()
        return msg


class AdminNewPersonalActivityCodePage(BasePage):
    """创建个人活动码页面"""
    input_code_name = "//label[contains(text(),'活动名称')]/../div/div[1]/input"
    btn_Choose_manager = "//span[contains(text(),'选择关联主理')]"
    input_check_manager = '//input[@placeholder = "搜索门店/主理人"]'
    input_choose_all_manager = "//span[contains(text(),'全部主理')]/../label/span/input"
    btn_Confirm = "//span[contains(text(),'确定')]"
    input_choose_channel = "//label[contains(text(),'选择渠道')]/../div/div/div[1]/div[1]/input"
    btn_choose_channel = "//span[contains(text(),'AAA·1 / BBB / CCC')]"
    input_label = "//label[contains(text(),'用户标签')]/../div/div/div[1]/div/input"
    btn_label = "//li[contains(text(),'测试人群包')]"
    input_greeting = "//textarea[@maxlength = '1000']"
    btn_save = "//div[@class='buttonContainer']/button[2]/span"
    Create_popover = "//div[@class='ivu-notice-title']"

    def create_code(self, personal_code_name, manager_name, channel_name, label_name, greeting_nr):
        """创建个人活动码"""
        self.iframe_enter(iframe_create_personalActivityCode)
        time.sleep(1)
        self.input(self.input_code_name, personal_code_name)
        self.click(self.btn_Choose_manager)
        self.input(self.input_check_manager, manager_name)
        self.find_element(self.input_check_manager).send_keys(Keys.ENTER)
        self.click(self.input_choose_all_manager)
        self.click(self.btn_Confirm)
        self.input(self.input_choose_channel, channel_name)
        self.click(self.btn_choose_channel, force=True)
        self.input(self.input_label, label_name)
        self.click(self.btn_label)
        self.input(self.input_greeting, greeting_nr)
        self.click(self.btn_save)
        self.click(self.btn_save)
        self.iframe_exit()
        msg = self.get_text(self.Create_popover)
        self.driver.switch_to.default_content()
        self.sleep(1)
        return msg


class AdminDealerActivityCodePage(BasePage):
    """门店活动码页面"""
    btn_createcode = "//span[contains(text(),'创建门店活码')]"
    input_codename = '//label[contains(text(),"活码名称")]/../div/div/input'
    btn_check = '//span[contains(text(),"查询")]'
    btn_delete = '//tbody[1]/tr/td[1]/div/div/span[3]'
    code_field2 = '//tbody[1]/tr/td[3]/div'
    btn_delete_check = '//span[contains(text(),"确定")]'
    popover_delete = '//div[@class="ivu-notice-title"]'

    def to_new_dealer_activity_code_page(self):
        """进入新增门店活动码页面"""
        self.iframe_enter(iframe_enter_storeActivityCode)
        self.click(self.btn_createcode)
        self.iframe_exit()
        return AdminNewDealerActivityCodePage(self.driver)


class AdminNewDealerActivityCodePage(BasePage):
    """创建门店活动码页面"""
    # input_code_name = "//label[contains(text(),'活动名称')]/../div/div[1]/input"
    input_code_name = "//input[@placeholder='请输入']"
    btn_Choose_manager = "//span[contains(text(),'选择关联主理')]"
    input_check_manager = '//input[@placeholder = "搜索门店/主理人"]'
    input_choose_all_manager = "//span[contains(text(),'全部主理')]/../label/span/input"
    btn_Confirm = "//span[contains(text(),'确定')]"
    input_choose_channel = "//label[contains(text(),'选择渠道')]/../div/div/div[1]/div[1]/input"
    btn_choose_channel = "//span[contains(text(),'AAA·1 / BBB / CCC')]"
    input_label = "//label[contains(text(),'用户标签')]/../div/div/div[1]/div/input"
    btn_label = "//li[contains(text(),'测试人群包')]"
    input_greeting = "//textarea[@maxlength = '1000']"
    btn_save = "//div[@class='buttonContainer']/button[2]/span"
    Create_popover = "//div[@class='ivu-notice-title']"

    def create_code(self, personal_code_name, manager_name, channel_name, label_name, greeting_nr):
        """创建门店活动码"""
        self.iframe_enter(iframe_create_storeActivityCode)
        self.input(self.input_code_name, personal_code_name)
        self.click(self.btn_Choose_manager)
        self.input(self.input_check_manager, manager_name)
        self.find_element(self.input_check_manager).send_keys(Keys.ENTER)
        self.click(self.input_choose_all_manager)
        self.click(self.btn_Confirm)
        self.input(self.input_choose_channel, channel_name)
        self.click(self.btn_choose_channel, force=True)
        self.input(self.input_label, label_name)
        self.click(self.btn_label)
        self.input(self.input_greeting, greeting_nr)
        self.click(self.btn_save)
        self.click(self.btn_save)
        self.iframe_exit()
        msg = self.get_text(self.Create_popover)
        self.iframe_exit()
        return msg
