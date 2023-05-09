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
        self.input('//input;;;[0]', "15999999")
        # print(text)
        # print(text[0])
        # self.input('//input[@placeholder="请输入手机号"]', phone)
        # # 输入密码
        # self.input('//input[@placeholder="请输入密码"]', pwd)
        # # 点击登录按钮
        # self.click("button;;;TAG_NAME")

        # # 打印登录信息
        # print(f"当前账户登录信息:\n"
        #       f"用户名:{phone}\n"
        #       f"密码:{pwd}"
        #       )
        #
        # self.click('/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[4]/div/span')
        # self.iframe_enter('//iframe[@src="/marketing/interactRadar/page"]')
        # self.input('//label[contains(text(),"雷达标题")]/../div/div/input', "二次创建互动雷达标题")
        # self.input('//label[contains(text(),"创建人")]/../div/div/input', "神秘人")
        # self.click('//span[contains(text(),"查询")]')
        # self.sleep(1)
        # self.click('//tbody[1]/tr/td[1]//div/div/span[3]')
        # self.iframe_exit()
        # self.refresh()
        # self.iframe_enter('//iframe[contains(@src,"/marketing/interactRadar/update")]')
        # print("dsd")
        # self.input('//input[@placeholder="请输入雷达标题"]', 1)
        # self.click('//button[contains(text(),"选择封面")]')
        # self.iframe_exit()
        # self.click('//div[@class = "app-grid-flex"]/div[2]/div/div[1]/img')
        # self.click('//div[@class = "app-grid-flex"]/div[2]/div/div[2]/label/span/input')
        # self.click('//span[contains(text(),"确定")]')
        # self.click('/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/label/span/input')
        # self.sleep(100)



        # a = self.get_text('//tbody[1]/tr[1]')
        # for i in ["zdh测试正常创建互动雷达标题", "zdh测试正常创建互动雷达链接标题", "zdh测试正常创建互动雷达链接摘要","神秘人"]:
        #     if i in a:
        #         print(5649)
        # print(a)
        time.sleep(1)
        # self.click("//span[contains(text(),'渠道活码工具')]")
        # self.sleep(0.5)
        # self.click("//span[contains(text(),'活动码')]")
        # self.sleep(0.5)
        # self.click("//span[contains(text(),'个人活动码')]")
        # self.iframe_enter(iframe_enter_personalActivityCode)
        # self.click("//span[contains(text(),'创建个人活动码')]")
        # self.iframe_exit()
        # self.sleep(2)
        # self.iframe_enter(iframe_create_personalActivityCode)
        # self.input("//label[contains(text(),'活动名称')]/../div/div[1]/input", "zdh测试个人活动码名称")
        # self.find_element("//label[contains(text(),'活动名称')]/../div/div[1]/input")
        # self.click("//span[contains(text(),'选择关联主理')]")
        # self.input('//input[@placeholder = "搜索门店/主理人"]', "田旭")
        # self.find_element('//input[@placeholder = "搜索门店/主理人"]').send_keys(Keys.ENTER)
        # self.click("//span[contains(text(),'全部主理')]/../label/span/input")
        # self.click("//span[contains(text(),'确定')]")
        # self.input("//label[contains(text(),'选择渠道')]/../div/div/div[1]/div[1]/input", "AAA·1 / BBB / CCC")
        # self.sleep(1)
        # self.click("//span[contains(text(),'AAA·1 / BBB / CCC')]", force=True)
        # self.sleep(1)
        # self.input("//label[contains(text(),'用户标签')]/../div/div/div[1]/div/input", "测试人群包")
        # self.click("//li[contains(text(),'测试人群包')]", force=True)
        # self.input("//textarea[@maxlength = '1000']", "zdh欢迎语")
        # self.click("//div[@class='buttonContainer']/button[2]/span")
        # self.click("//div[@class='buttonContainer']/button[2]/span")
        # self.iframe_exit()
        # msg = self.get_text("//div[@class='ivu-notice-title']")
        # print(msg)
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[0])
        # time.sleep(100)



        # self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[1]')
        # driver.find_element_by_xpath("//标签名[contains (@属性，‘属性值’)]")
        # driver.find_element_by_xpath("//标签名[starts-with (@属性，‘属性值’)]")
        # driver.find_element_by_xpath("//标签名[end-with (@属性，‘属性值’)]")
        # msg = self.get_text("//div[@class='ivu-notice-title']")
        # print(msg)
        # k = self.get_text('//div[@class = "ivu-notice-notice-content"]')
        # print(k)
        # self.sleep(1)
        # self.click("//span[contains(text(),'渠道活码工具')]")
        # self.sleep(0.5)
        # self.click("//span[contains(text(),'活动码')]")
        # self.sleep(0.5)
        # self.click("//span[contains(text(),'个人活动码')]")
        # self.driver.refresh()
        # self.sleep(1)
        # self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[1]')

        # self.input('//label[contains(text(),"活码名称")]/../div/div/input', "zdh测试个人活动码名称_蔡新强")
        # self.click('//span[contains(text(),"查询")]')
        # time.sleep(1)
        # a = self.get_text('//tbody[1]/tr/td[3]/div')
        # a = self.driver.page_source
        # if "zdh测试个人活动码名称_蔡新强" in a:
        #     print("dwfwfw")
        # print(a)
        # self.click('//tbody[1]/tr/td[1]/div/div/span[3]')
        # self.iframe_exit()
        # self.click('//span[contains(text(),"确定")]')
        # a = self.get_text('//div[@class="ivu-notice-title"]')
        # print(a)
        # print(self.driver.page_source)
        # if "zdh测试个人活动码名称_蔡新强" in self.driver.page_source:
        #     print(9999)
        # d = self.get_text("/html/body/div[4]/div/div[1]/div/div[1]")
        # print(d)
        # time.sleep(100)
        self.quite()
        """
        self.click("/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[4]/div/span")
        time.sleep(1)
        self.driver.refresh()
        self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[1]')
        self.click("//span[contains(text(),'渠道管理')]")
        self.driver.refresh()
        self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[1]')
        self.click("//span[contains(text(),'创建渠道')]")
        self.driver.refresh()
        self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[1]')
        self.input('//input[@placeholder="请输入渠道名称"]', "测试渠道")
        self.click("//span[contains(text(),'选择关联门店')]")
        self.input('//input[@placeholder="请输入门店名称回车查询"]', "五件套店U2")
        self.find_element('//input[@placeholder="请输入门店名称回车查询"]').send_keys(Keys.ENTER)
        self.click("//span[contains(text(),'全部门店')]/../span[1]")
        self.click("//span[contains(text(),'五件套大区1')]/../span[1]")
        self.click("//span[contains(text(),'五件套店U2')]/../label/span/input")
        self.click("//span[contains(text(),'确定')]")
        self.click("//span[contains(text(),'保存')]")
        """


if __name__ == '__main__':
    # while True:
    log = Login_zj()
    log.login("https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr", "19542812247", "LEdiiUpV")
