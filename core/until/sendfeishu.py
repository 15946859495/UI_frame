# -*- coding: utf-8 -*-
""" 
@Filename:  core/testcase/test_web.py 
@Author:    小蔡 
@Time:      2022/12/7 10:21
@Describe: ... 
"""
import datetime
import requests
import json
from core.until.time_conversion import ms_to_date


def sendFeiShu(ip, report_path):
    try:
        with open(report_path, encoding='utf-8') as data:
            case_data_dict = json.loads(data.read())
        failed = case_data_dict['statistic']['failed']
        broken = case_data_dict['statistic']['broken']
        skipped = case_data_dict['statistic']['skipped']
        passed = case_data_dict['statistic']['passed']
        unknown = case_data_dict['statistic']['unknown']
        total = case_data_dict['statistic']['total']
        pass_rate = str(passed/total*100)[:5]
        start = str(
            datetime.datetime.fromtimestamp(case_data_dict['time']['start'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S'))
        stop = str(
            datetime.datetime.fromtimestamp(case_data_dict['time']['stop'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S'))
        duration = ms_to_date(case_data_dict['time']['duration'])
        data = f"执行时间：\n{start} - {stop}\n耗时:{duration}\n执行通过用例数：{passed}\n执行失败用例数：{failed}\n" \
               f"阻塞用例数：{broken}\n执行跳过用例数：{skipped}\n未知用例数：{unknown}\n用例总数：{total}\n用例执行通过率：{pass_rate}%\n\n"
        # 机器人webhook地址
        robot_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/403efa07-dcc8-4332-8e21-010431c228d5'
        # 发送内容
        payload = json.dumps({
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": f"自动化测试用例执行完毕",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": data
                                },
                                {
                                    "tag": "text",
                                    "text": "本地局域网测试报告地址如下：" + "\n"
                                },
                                {
                                    "tag": "text",
                                    "text": "http://" + ip + ":666"
                                }
                            ]
                        ]
                    }
                }
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", robot_url, headers=headers, data=payload).json()
        print("测试报告发送成功" if response['StatusCode'] == 0 and response[
            'StatusMessage'] == "success" else "测试报告发送失败")
    except Exception as why:
        print(f"发送测试报告异常，异常日志如下：\n"
              f"{why}")


if __name__ == '__main__':
    sendFeiShu()
