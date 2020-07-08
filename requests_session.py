#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
* @Author:     sky
* @date:       2020-07-08
* @version:    v1.0
* @description:用session模拟登录GitHub
"""

import requests
import re


class Formdata:
    # 存储从静态页面中解析出的表单数据
    # 直接填写的为固定值，否则为变化值
    commit = 'Sign in'
    token = ''
    ga_id = '324439181.1591862013'
    webauthn_support = 'supported'
    webauthn_iuvpaa_support = 'unsupported'
    return_to = ''
    required_field_name = ''
    time_stamp = ''
    timestamp_secret = ''


class Github:
    def __init__(self, username, password):
        # 头部数据
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
        }
        self.session = requests.session() # 创建session对象
        self.username = username
        self.password = password
    
    def get_login_data(self):
        # 请求静态页面数据，用于解析表单中需要的部分数据
        login_url = 'https://github.com/login'
        response = self.session.get(login_url, headers=self.headers).content.decode()
        return response
    
    def parse_data(self, response):
        # 将解析出来的数据存储到Formdata类变量中
        Formdata.token = re.findall('name="authenticity_token" value="(.*?)"', response)[0]
        Formdata.required_field_name = re.findall('<input class="form-control" type="text" name="(.*?)" hidden="hidden"', response)[0]
        Formdata.time_stamp = re.findall('name="timestamp" value="(.*?)"', response)[0]
        Formdata.timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)"', response)[0]
    
    def construct_form_data(self):
        # 构造表单数据字典
        form_data = {}
        form_data['commit'] = Formdata.commit
        form_data['authenticity_token'] = Formdata.token
        form_data['ga_id'] = Formdata.ga_id
        form_data['login'] = self.username
        form_data['password'] = self.password
        form_data['webauthn-support'] = Formdata.webauthn_support
        form_data['webauthn-iuvpaa-support'] = Formdata.webauthn_iuvpaa_support
        form_data['return_to'] = Formdata.return_to
        form_data[Formdata.required_field_name] = ''
        form_data['timestamp'] = Formdata.time_stamp
        form_data['imestamp_secret'] = Formdata.timestamp_secret
        return form_data
    
    def post_form_data(self, data):
        # 发送post请求，提交表单数据
        post_url = "https://github.com/session"
        response = self.session.post(post_url, headers=self.headers, data=data).content.decode()
        return response
    
    def login_status(self):
        # 验证登录是否成功
        url = "https://github.com/{}".format(self.username)
        response = self.session.get(url)

        with open('github.html', 'wb') as f:
            f.write(response.content)
        
        # 验证是否成功
        name = re.findall('<title>(.*?)</title>', response.content.decode())[0]
        print(name)
        if name == self.username:
            print('哈哈哈，登录成功了呢')
        else:
            print('哦吼，登录失败了呢')
    
    def run(self):
        # 获取数据
        response = self.get_login_data()
        # 解析数据并构造表单
        self.parse_data(response)
        form_data = self.construct_form_data()
        # 发送post请求进行登录
        response1 = self.post_form_data(form_data)
        # 验证登录状态
        self.login_status()


if __name__ == "__main__":
    username = input("请输入Github用户名：")
    password = input("请输入密码：")
    github = Github(username, password)
    github.run()