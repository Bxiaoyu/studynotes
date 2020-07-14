#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
* @Author:     sky
* @date:       2020-07-14
* @version:    v1.0
* @description:纯python模拟加密向有道翻译提交数据
"""
import hashlib
import requests
import time
import random
import json


class Youdao:

    def __init__(self, word):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=317842497@10.169.0.102; JSESSIONID=aaa1S8oKlsfDh8togbmnx; OUTFOX_SEARCH_USER_ID_NCOO=1727057075.799137; ___rl__test__cookies=1594712284621',
            'Referer': 'http://fanyi.youdao.com/'

        }
        self.formdata = None
        self.word = word
    
    def generate_formdata(self):
        """
            ts: r = "" + (new Date).getTime(),
            salt: ts + parseInt(10 * Math.random(), 10);,
            sign: n.md5("fanyideskweb" + e + i + "mmbP%A-r6U3Nw(n]BjuEU")
        }
        """
        # 这几个参数是由网站的js动态加密生成的（变化值），这里用python来模拟实现达到同样的效果，
        # 免去用第三方js加载模块
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0, 9))
        temp_str = "fanyideskweb" + self.word + salt + "mmbP%A-r6U3Nw(n]BjuEU"
        md5 = hashlib.md5()
        md5.update(temp_str.encode())
        sign = md5.hexdigest()

        self.formdata = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': '02a6ad4308a3443b3732d855273259bf',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
    
    def get_data(self):
        #print(self.formdata)
        response = requests.post(self.url, data=self.formdata, headers=self.headers)
        return response
    def parse_data(self, response_data):
        data = json.loads(response_data.content.decode())
        try:
            result = data['translateResult'][0][0]['tgt']
            return result
        except:
            return ""

    def run(self):
        # url
        # headers
        # formdata
        self.generate_formdata()
        # 发送请求，获取数据
        response = self.get_data()
        # 解析数据
        print("翻译结果：{}".format(self.parse_data(response)))


if __name__ == "__main__":
    word = input("请输入关键字：")
    yd = Youdao(word)
    yd.run()
