# -*- coding: utf-8 -*-
""" 
@Filename:  /sss
@Author:    小蔡 
@Time:      2023/2/13 11:31
@Describe: ... 
"""

"""
 # 点击创建雷达按钮
self.iframe_exit()
# time.sleep(100)
self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[3]')
# self.iframe_enter("frame-3;;;ID")
self.input(lz.Radar_title_input_box, "Radar_title13")  # 输入雷达标题
self.input(lz.Radar_link_input_box, "https://scrm-uat.immotors.com/marketing/interactRadar/create?_tgt=fr")  # 输入雷达链接
self.input(lz.Link_title_input_box, "Link_title")  # 输入链接标题
self.input(lz.Link_summary_input_box, "Link_summary")  # 输入链接摘要
self.click(lz.Select_cover_button)  # 点击选择封面按钮
self.iframe_exit()
self.click(lz.img)
self.click(lz.img_check_box)
self.click(lz.Confirm_button)
self.iframe_enter("frame-3;;;ID")
self.click(lz.Create_confirm_button)
self.iframe_exit()
mgs = self.get_text(lz.Create_popover)
time.sleep(3)
self.click("/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[4]/div/span")
time.sleep(2)
self.iframe_enter("frame-2;;;ID")
time.sleep(2)
print(2)
self.click(lz.Create_Radar_button)  # 点击创建雷达按钮
"""
# time.sleep(1)
# self.input('//label[contains(text(),"雷达标题")]/../div/div/input',"随便输的别介意")
# self.input('//label[contains(text(),"创建人")]/../div/div/input',"嘿嘿嘿")
# self.click('//span[contains(text(),"查询")]')
# self.click('//span[contains(text(),"重置")]')
# time.sleep(3)
# self.input('//label[contains(text(),"雷达标题")]/../div/div/input', "Radar_title10")
# self.input('//label[contains(text(),"创建人")]/../div/div/input', "神秘人")
# self.click('//span[contains(text(),"查询")]')
# a = self.get_text('//tbody[1]/tr/td[2]/div/div')
# print(a)
# time.sleep(1)
# self.click('//tbody[1]/tr/td[1]/div/div/span[4]')
# self.iframe_exit()
# print("切完了")
# self.click('//div[@class="ivu-modal-confirm-footer"]/button[2]')
# time.sleep(1)
# b = self.get_text('//div[contains(text(),"删除成功")]')
# print('b')
# time.sleep(5)
# self.click('/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[11]/div/div/span')
# time.sleep(1)
# self.click('//span[contains(text(),"席位管理")]')
# self.driver.refresh()
# self.iframe_enter('/html/body/div[1]/div[2]/div[2]/div[2]/div/iframe[1]')
# self.click('//span[contains(text(),"导出")]')
# time.sleep(100)
# self.quite()
