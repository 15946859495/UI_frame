# -*- coding: utf-8 -*-
""" 
@Filename:  core/until/tool
@Author:    小蔡 
@Time:      2023/2/6 14:06
@Describe: ... 
"""
import logging
import os
import time

import xlrd

from core.until.data import *


def clear_download_file(file_path, file_name):
    """删除文件"""
    os.remove(file_path + '\\' + file_name)


def check_download_file(file_path, file_name, load=1):
    """检查文件是否存在"""
    status = False
    try:
        if os.path.exists(file_path):
            time.sleep(int(load))
            for file in os.listdir(file_path):
                if file_name in file:
                    status = True
            if status:
                return True
            else:
                return False
    except Exception:
        logging.info("The file is not exist！Please check the code！")


def read_excel(path_excel):
    """读取列表第一行数据"""
    table = xlrd.open_workbook(path_excel)
    table_sheet = table.sheets()[0]
    table_list = table_sheet.row_values(0)
    return table_list


def read_excel_all(path_excel):
    """读取列表第一行数据"""
    table = xlrd.open_workbook(path_excel)
    table_sheet = table.sheets()[0]
    text_list = []
    for row in range(table_sheet.nrows):
        table_list = table_sheet.row_values(row)
        a = [i.replace(u'\xa0', '').strip() for i in table_list if i != '']
        text_list.append(a)
    return text_list


if __name__ == '__main__':
    read_excel_all("C:\\Users\\\wangy\\Downloads\\运营号数据.xlsx")
    # print(check_download_file("C:\\Users\\\wangy\\Downloads", "运营号数据.xlsx"))
    # print(read_excel("C:\\Users\\\wangy\\Downloads\\运营号数据.xlsx"))
    # clear_download_file("C:\\Users\\\wangy\\Downloads", "互动雷达.xlsx")
