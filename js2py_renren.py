#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
* @Author:     sky
* @date:       2020-07-14
* @version:    v1.0
* @description:用js2py模块获取js代码加密数据模拟登录人人网
"""
import requests
import js2py
import json


def login():
    # 创建session对象
    session = requests.session()
    # 设置请求头
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    }
    # 发送获取公钥数据包的get请求
    response = session.get('http://activity.renren.com/livecell/rkey')
    # 创建n
    n = json.loads(response.content)['data']
    # 创建t
    t = {
        'password':'123456'
    }
    # 获取前置js代码
    rsa_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js').content.decode()
    bigint_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js').content.decode()
    barrett_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js').content.decode()
    # 创建js环境对象
    context = js2py.EvalJs()
    # 将变量和Js代码加载到环境对象中执行
    context.execute(rsa_js)
    context.execute(bigint_js)
    context.execute(barrett_js)
    context.n = n
    context.t = t

    # 将关键js代码放到环境对象中执行
    pwd_js = """
    t.password = t.password.split("").reverse().join(""),
    setMaxDigits(130);
    var o = new RSAKeyPair(n.e, "", n.n),
    r = encryptedString(o, t.password);
    """
    context.execute(pwd_js)
    # 获取加密密码
    print(context.r)
    # 构建formdata
    formdata = {
        'phoneNum':'17173805860',
        'password': context.r,
        'c1':-100,
        'rKey': n['rkey']
    }
    # 发送post请求，模拟登录
    response1 = session.post('http://activity.renren.com/livecell/ajax/clog', data=formdata)
    # 验证
    print(response1.content.decode())


if __name__ == "__main__":
    login()