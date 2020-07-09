#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
* @Author:     sky
* @date:       2020-07-09
* @version:    v1.0
* @description:百度贴吧练习xpath解析
"""
import requests
from lxml import etree


class Tieba(object):
    def __init__(self, name):
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw={}".format(name)
        # 浏览器的内核版本会对爬取内容有影响，对于高端浏览器网站注释了的一些内容依旧能解析出来，低端的则解析不出来，所以考虑换头
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt)'
        }
    
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content
    
    def parse_data(self, data):
        # 不换请求头，直接将数据中的注释替换掉
        # data = data.decode().replace('<!--', '').replace('-->', '')
        html = etree.HTML(data)

        el_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # print(len(el_list))

        data_list = []
        for e in el_list:
            temp = {}
            temp['title'] = e.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + e.xpath('./@href')[0]
            data_list.append(temp)
        
        # 循环翻页
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(), "下一页>")]/@href')[0]
        except:
            next_url = None
        return data_list, next_url
    
    def save_data(self, data_list):
        for data in data_list:
            print(data)


    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送请求，获取响应
            data = self.get_data(self.url)
            # 从响应中提取数据(数据和翻页用的url)
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            # 判断是否结束
            print(next_url)
            if next_url == None:
                break

if __name__ == "__main__":
    tb = Tieba('李毅吧')
    tb.run()