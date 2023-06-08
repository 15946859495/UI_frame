"""
@Filename:  core/testcase/test_login.py
@Author:    小蔡 
@Time:      2022/11/14 10:04
@Describe: ... 
"""
import io
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from core.until.Commonlib import Commonshare
from core.until.element import *
from selenium.webdriver.common import alert



class Login_zj(Commonshare):
    def login(self, url, phone, pwd):
        lz = Login_zj
        # self.get('https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr')
        # self.get('https://scrm-prod.immotors.com/marketing/dataBoard/page?_tgt=fr')
        self.get(url)
        # 输入手机号
        self.input('//input[@placeholder="请输入手机号"]', phone)
        # 输入密码
        self.input('//input[@placeholder="请输入密码"]', pwd)
        # 点击登录按钮
        self.click("button;;;TAG_NAME")
        self.click('//span[text() = " 管  理"]')
        self.click('//span[contains(text(),"席位管理")]')
        self.iframe_enter('//iframe[@src="/dms/devicePc/page"]')
        # self.assert_list_export('//tbody[1]/tr')
        # self.hd(5)
        # element = self.find_element('//span[text()="门店"]')
        # self.driver.execute_script('arguments[0].scrollIntoView();', element)
        # element = self.find_element('//span[text()="分配状态"]')
        # self.driver.execute_script('arguments[0].scrollIntoView();', element)
        a = self.get_text('//table')
        dd = []
        msg = self.driver.find_elements(By.XPATH, '//tbody[1]/tr')
        for i in msg:
            i = i.text.split('\n')
            dd.append(i)
        print(dd)
        self.sleep(10)
        self.quite()


if __name__ == '__main__':
    # while True:
    log = Login_zj()
    log.login("https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr", "19542812247", "LEdiiUpV")
