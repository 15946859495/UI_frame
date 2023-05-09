# -*- coding: utf-8 -*-
""" 
@Filename:  core/testcase/test_excel
@Author:    小蔡 
@Time:      2023/2/24 11:26
@Describe: ... 
"""
from pathlib import Path

from core.until.cases import *
from core.until.datas import load_case_by_excel

i = 0

# 多Excel 一下代码全部循环
# for file in Path("temp").glob("test_*.xlsx"):
for file in Path("core/testcase").glob("test_*.xlsx"):

    suite_list = load_case_by_excel(file)  # 从excel加载数据
    test_xiaocai = create_pytest_case(suite_list)  # test开头的列表

    for _test in test_xiaocai:
        i += 1
        globals()[f"test_{i}"] = _test  # test 开头的函数
