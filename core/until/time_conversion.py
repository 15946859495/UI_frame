# -*- coding: utf-8 -*-
""" 
@Filename:  core/until/time_conversion
@Author:    小蔡 
@Time:      2023/3/9 18:00
@Describe: ... 
"""


def ms_to_date(millis):
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    hours = int(hours)
    days = (millis / (1000 * 60 * 60 * 24))
    days = int(days)
    lay = millis - hours * 1000 * 60 * 60 - minutes * 1000 * 60 - seconds * 1000
    ms = f"{int(lay)}ms" if days == hours == minutes == 0 else ""
    s = f"{int(seconds)}s" if seconds else ""
    m = f"{int(minutes)}m" if minutes else ""
    h = f"{int(hours)}h" if hours else ""
    d = f"{int(days)}d" if days else ""
    data = f"{d}{h} {m} {s} {ms}"

    return data
