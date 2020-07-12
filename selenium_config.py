#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:      sky
@date:        2020-07-11
@description: chrome配置无头浏览器
"""
from selenium import webdriver

url = "http://www.baidu.com"

# 创建配置对象
opt = webdriver.ChromeOptions()
# 添加配置参数
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
# 使用代理
opt.add_argument('--proxy-server=http://119.179.174.121:8060')
# 更换user-agent
opt.add_argument('--user-agent=Mozilla/5.0 python37')
# 创建浏览器对象的时候添加配置对象
driver = webdriver.Chrome(chrome_options=opt)

driver.get(url)

driver.save_screenshot("baidu.png")