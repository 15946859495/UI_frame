"""
@Filename:  core/testcase/test_login.py
@Author:    小蔡
@Time:      2022/09/28 20:30
@Describe: ...
"""
import json

import requests


# def img2code(file):
#     url = "http://47.106.70.21:5516/auth/login"
#
#     data = {
#         "user": "pengjiangchun",
#         "pass2": "3eb5f9a3a31fb000969e696d7c3cc71f",  # 密码的md5值
#         "sofid": "mashang",  # 个人中心设置的软件id
#         "codetype": 1902,
#     }
#     files = {"userfile": open(file, "rb")}
#     resp = requests.post(url, data=data, files=files)
#
#     res = resp.json()
#     if res["err_no"] == 0:
#         code = res["pic_str"]
#         print("识别成功", code)
#         return code
#     else:
#         print("识别失败")
#         return False


def save_cookies(driver):
    """保存cookies到本地文件"""
    cookies = driver.get_cookies()  # 获取cookies

    with open("temp/cookies.json", "w") as f:
        f.write(json.dumps(cookies))


def load_cookies(driver):
    """从本地文件加载cookies"""

    driver.get("https://scrm-uat.immotors.com/marketing/dataBoard/page?_tgt=fr")
    try:
        with open("temp/cookies.json") as f:
            cookies = json.loads(f.read())

        for cookie in cookies:
            driver.add_cookie(cookie)  # 使用cookies

        driver.refresh()  # 刷新页面，向服务器发送cookeis
    except:
        pass


def is_login(driver):
    """是否已经登录"""
    if "请输入密码" in driver.page_source:
        print("需要登录")
        return False
    else:
        print("已经登录"+'\n')
        return True
