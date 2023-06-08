# -*- coding: utf-8 -*-
""" 
@Filename:  /test
@Author:    小蔡 
@Time:      2023/5/6 10:15
@Describe: ... 
"""
a = ['--', '罗老师', '17890873456', '福建', '福州', '智慧']
x = ""
for i in a:
    x += i.replace("'", '')+','
print(x)