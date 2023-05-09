# -*- coding: utf-8 -*-
""" 
@Filename:  core/until/Makedir
@Author:    小蔡 
@Time:      2023/3/10 9:51
@Describe: ... 
"""
import os
import time


def mkdir():
    files_name = "reports/report_" + time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    os.mkdir(files_name)  # 配置文件未指定报告存放路径，以当前时间为创建一个存放报告的目录
    report_path = files_name + "/widgets/summary.json"
    return files_name, report_path
