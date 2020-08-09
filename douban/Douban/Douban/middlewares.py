# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
import base64
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from scrapy import signals
from Douban.settings import USER_AGENT_LIST, PROXY_LIST

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 定义一个中间件类
class RandomUserAgent(object):

    def process_request(self, request, spider):
        # print(request.headers)
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua


class RandomProxy(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)

        if 'user_passwd' in proxy:
            # 对帐号密码进行编码
            b64_up = base64.b64encode(proxy['user_passwd'].encode()) # 传入的是bytes类型
            # 设置认证
            request.headers['proxy-Authorization'] = 'Basic ' + b64_up.decode() # Basic后面要跟空格
            # 设置代理
            request.meta['proxy'] = proxy['ip_port']
        else:
            # 设置代理
            request.meta['proxy'] = proxy['ip_port']


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        url = request.url

        if "daydata" in url:
            driver = webdriver.Chrome()

            driver.get(url)
            time.sleep(3)
            data = driver.page_source

            driver.close()

            # 创建响应对象
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)

            return res