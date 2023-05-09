# -*- coding: utf-8 -*-
""" 
@Filename:  core/until/settings
@Author:    小蔡 
@Time:      2023/2/24 11:26
@Describe: ... 
"""
import os
import time
from configparser import SafeConfigParser

from iniconfig import IniConfig

BOOLEAN_STATES = SafeConfigParser.BOOLEAN_STATES


def load_uitest_ini(file):
    ini = IniConfig(file)  # 加载文件内容
    ui_ini = ini["uitest"]

    # print(ui_ini.get("wait_max", "20"))

    d = {
        "driver_type": ui_ini.get("driver_type", "chrome"),
        "wait_max": float(ui_ini.get("wait_max", "10")),
        "wait_poll": float(ui_ini.get("wait_poll", "0.5")),
        "allure_gen": BOOLEAN_STATES[(ui_ini.get("allure_gen", "true"))],
        "allure_show": BOOLEAN_STATES[ui_ini.get("allure_show", "true")],
        "allure_path": ui_ini.get("allure_path", "report"),
    }

    return d


settings = load_uitest_ini(r"pytest.ini")  # 配置项目设置为全局变量
if __name__ == "__main__":
    print(settings)
