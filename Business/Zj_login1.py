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
        self.click("//span[contains(text(),'人群包')]")
        self.iframe_enter('//iframe[@src="/im/group/page"]')
        self.click("//span[contains(text(),'创建人群包')]")
        self.iframe_exit()
        self.input('//input[@placeholder="人群包名称限20字"]', 'Zdh测试人群包名称')
        self.input('//textarea', 'zdh测试人群包名称')
        self.click('//span[text()="添加"]')
        self.input('//input[@placeholder="请选择一级标签，支持键入搜索"]', '临时人群包')
        self.click('//li[text()="临时人群包"]')
        self.input('//input[@placeholder="请选择二级标签，支持键入搜索"]', '测试人群包')
        self.click('//li[text()="测试人群包"]')
        self.click('//span[text()="确定"]')
        self.sleep(10)


if __name__ == '__main__':
    # while True:
    log = Login_zj()
    log.login("https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr", "19542812247", "LEdiiUpV")
