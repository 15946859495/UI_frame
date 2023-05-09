# -*- coding: utf-8 -*-
""" 
@Filename:  core/until/Get_ip
@Author:    小蔡 
@Time:      2023/3/10 9:48
@Describe: ... 
"""
import socket


def get_ip():
    ip = 0
    ips = socket.getaddrinfo(socket.gethostname(), None)
    for i in range(0, len(ips)):
        if "192.168" in ips[i][4][0]:
            ip = ips[i][4][0]
            break
    print(f"{ip=}")
    return ip


if __name__ == '__main__':
    get_ip()
