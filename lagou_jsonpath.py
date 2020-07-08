#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
* @Author:     sky
* @date:       2020-07-08
* @version:    v1.0
* @description:测试jsonpath模块，提取拉钩网的城市数据
"""
import requests
import jsonpath
import json

def get_lagou_data():
    # 拉钩网城市数据
    url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    dict_data = json.loads(response.content)

    # 提取出所有拼音以A开头的城市名
    print(jsonpath.jsonpath(dict_data, "$..A..name"))

    # 提取出所有城市
    print(jsonpath.jsonpath(dict_data, "$..name"))

if __name__ == "__main__":
    get_lagou_data()

