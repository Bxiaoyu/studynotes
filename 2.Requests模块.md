# Requests模块

> 知识点：
> * 掌握headers参数的使用
> * 掌握发送带参数的请求
> * 掌握headers中携带cookie
> * 掌握cookie参数的使用
> * 掌握cookiejar的转换方法
> * 掌握超时参数timeout的使用
> * 掌握代理ip参数proxies的使用
> * 掌握使用verify参数忽略CA证书
> * 掌握requests模块发送post请求
> * 掌握利用requests.session进行状态保持

## 1. 简单使用requests模块

```python
import requests

url = "https://www.baidu.com"
# 向目标url发送GET请求
response = requests.get(url)
# 打印响应内容
# print(response.text)
print(response.content.decode()) # 注意这里要解码
```

## 2. response响应对象

### 2.1 response.text和response.content的区别

* response.text
  * 类型：str
  * 解码类型：requests模块自动根据HTTP头部对应的编码做出有根据的推测，推测文本的编码

* response.content
  * 类型：bytes
  * 解码类型：没有指定，可自行指定

### 2.2 通过对response.content进行decode，来解决中文乱码

* response.content.decode() 默认utf-8
* response.content.decode('GBK')
* 常见的编码字符集
  * utf-8
  * gbk
  * gb2312
  * ascii
  * iso-8859-1

### 2.3 response响应对象的其它常用属性或方法

> response是发送请求获取的响应对象; response响应对象中除了text，content获取响应内容外还有其它的常用方法或属性

* response.url 响应的url，有时候响应的url和请求的url并不一致
* response.status_code 响应状态码
* response.requests.headers 响应对象的请求头
* response.headers 响应头
* response.requests.cookies 响应对应请求的cookie；返回cookieJar类型
* response.cookies 响应的cookie（经过set-cookie动作；返回cookieJar类型）
* response.json() 自动将json字符串类型的响应头转换为python对象（dict或list）

## 3. 发送GET请求

### 3.1 发送带请求头的请求

```python
import requests

# 构造请求头字典，需要用到的请求头内容都可以加进来
headers = {"User-Agent":"my-app/0.0.1"}

url = "https://www.baidu.com"

response = requests.get(url, headers=headers)
```

### 3.2 发送带参数的请求

> 在搜索的时候，url地址中经常会有一个？，这个问号后面的就是请求参数，又叫做查询字符串

#### 3.2.1 在url中携带参数

直接对含有参数的url发起请求

```python
import requests

# 构造请求头字典，需要用到的请求头内容都可以加进来
headers = {"User-Agent":"my-app/0.0.1"}

url = "https://www.baidu.com/s?wd=python"

response = requests.get(url, headers=headers)
```

#### 3.2.2 通过params携带参数字典

1. 构建请求参数字典
2. 发送请求的时候带上参数字典，参数字典设置给params

```python
import requests

# 构造请求头字典，需要用到的请求头内容都可以加进来
headers = {"User-Agent":"my-app/0.0.1"}

url = "https://www.baidu.com/s?"

# 请求参数是一个字典
kw = {'wd':'python'}

response = requests.get(url, headers=headers, params=kw)
```

### 3.3 在headers参数中携带cookie

> 网站经常利用请求头中的Cookie字段来做用户访问状态的保持，那么可以在headers参数中添加Cookie，模拟普通用户的请求。

```python
import requests

# 构造请求头字典，需要用到的请求头内容都可以加进来
headers = {"User-Agent":"my-app/0.0.1",
           "Cookie":"Cookie内容"
}

url = "https://github.com/exile-morganna"

response = requests.get(url, headers=headers)
```

### 3.4 cookies参数的使用

> 我们可以在headers参数中携带cookie,也可以使用专门的cookies参数

**注意：** cookie一般是有过期时间的，一旦过期需要重新获取

```python
import requests

# 构造请求头字典，需要用到的请求头内容都可以加进来
headers = {"User-Agent":"my-app/0.0.1"}

url = "https://github.com/exile-morganna"

temp = "_octo=GH1.1.508598558.1591861842; _ga=GA1.2.324439181.1591862013; tz=Asia%2FShanghai; _device_id=e85d35e3c38434f731f798724a5e530f; has_recent_activity=1; _gat=1; user_session=i4aqQYxPyAw65msGdC9a4k7mnqR4oo_oP4Ry7057av15YyBy; __Host-user_session_same_site=i4aqQYxPyAw65msGdC9a4k7mnqR4oo_oP4Ry7057av15YyBy; logged_in=yes; dotcom_user=Bxiaoyu; _gh_sess=gCJEwTLNuMKv1WAiw6v6z%2B6qSTjOUuH5GIsoEVF7TNzYfiXVNqkMFq%2Fq9ESN60wJZeJyd4KgnO0y6gYmpCi30JNaSUALL%2FGQSZeaZnpQ9I9wAQlXfkC0wZVbOlFy7KruXUdvJjRzmP2bW0Vme6rOLF9ULnOSzT4G%2F0yqCl71JvFHoa2I0KfP9sOLTj5Es1g6CtxUEUd7xUcKm2essA4%2F74RnsOK14gxc8PXaDEW2oEeQFqXN7DW6P00Ixzndf0ZLcQa6tsLdlnBjtnfTAtM8PO%2FEAWxyOUtSYxjnYj24ajS4gmHAROpp%2Fqvk%2Fa82SVIPUcQlC%2BEV0OiWSfbzcbGHyG7tGcmJ%2BVPYUfUXES3slCAv7%2B2rYQQG3IRq2tuLhhU6V%2BXsg3OgZLB6DGGySToOLLbgruHHVF1Oa8iVdPO8UFuYsnquA2D%2F7Zax%2FnRP2Xid1%2F1AKfcoREh2AxkbmDDWZ5dRFYgGV71FEf1XJgfBnIhueFnHSm5LPfNdIs90dgSPgjr7TmA2HckHBNJokVCRQswouVhws0JOJHNVD7Ma7aLtMRqtrUB9VW8YNlH8Y4kHFmuQgz8FPWG6UgekSFsHxHKelCllXiCFeE7fYkPwdC9exiOtpY19sKBK%2BGUm17d1D7eL07PeL%2FNapGxCz%2F%2BxKw%2BnI1UCa8%2BKGAGGmWyA1Iw0zZt778q2CEyl7cXEg72b0CdNLwNeQ0Ha16YspQUJEStR4zItx%2F4oz7xhQfHYkZ8SJtUrtcGBmOmhjBY5jANXD6kt5yo%2FoXK3iuWIiaQ67hAyS0%2Bnl%2FrgjgWtNQ8kHLkaP7BrRbt7Akfm33PpTR66idgbkXNk82PdlRqA4IjHzgyQR4k%3D--pVzfNTzan9%2BgrSYO--Le5VINQZsQt5p8p3ClI1Ag%3D%3D"

cookies_list = temp.split("; ")

# 用字典推导式构造字典
cookies = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookies_list}

response = requests.get(url, headers=headers, cookies=cookies)
```

#### 3.4.1 cookieJar对象转换为cookies字典的方法

> 使用requests获取的response对象，具有cookie属性。该属性值是一个cookieJar类型，包含对方服务器设置在本地的cookie

1.转换方法

```python
import requests

# cookieJar转为dict
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)

# dict转为cookieJar
cookie_jar = requests.utils.cookiejar_from_dict(cookies_dict)
```

2.其中，response.cookies返回的就是cookieJar类型的对象

3.requests.utils.dict_from_cookieJar函数返回cookies字典

### 3.5 超时参数timeout的使用

> 如果一个请求很久没有结果，会影响效率，可以对请求进行强制要求，让它在特定的时间内返回结果，否则就报错

1.超时参数timeout的使用方法

```python
response = requests.get(url, timeout=3)
```

2.timeout=3表示：发送请求3秒内返回结果，否则就抛出异常

### 3.6 ip代理

#### 3.6.1 代理基础知识

1.什么是代理
代理ip的一个ip，指向的是一个代理服务器，作用是转发请求

2.正向代理和反向代理
以知不知道最终服务器的地址作为判断标准（正向代理知道，反向代理不知道）

3.代理ip的分类

* 按匿名度分
  1. 透明代理
  2. 匿名代理
  3. 高匿代理（效果最佳）
* 按协议分
  1. http代理
  2. https代理
  3. socks隧道代理

#### 3.6.2 proxies代理参数的使用

> 为了迷惑服务器，为了防止频繁向一个域名发送请求被封ip，我们需要使用代理ip

* 用法

```python
response = requests.get(url, proxies=proxies)
```

* proxies的形式：字典
* 例如：
自己选择协议类型

```python
proxies = {
    'http':'http://192.168.10.1:9527',
    'https':'https://192.168.10.1:9527'
    }
```

**注意：** 代理使用成功不会有任何报错，能成功获取响应内容；如果失败，要么停滞，要么报错

### 3.7 使用verify参数忽略CA证书

 > 使用浏览器上网的时候，有时候会出现以下提示：

 ![verify](/image/verify.png)

* 原因：该网站的CA证书没有经过【受信任的根证书颁发机构】的认证

#### 3.7.1 运行代码查看向不安全的链接发起请求的效果

> 运行以下代码会抛出ssl.CertificateError...字样的异常

 ```python
 import requests

url = 'https://sam.huat.edu.cn:8443/selfservice/'
response = requests.get(url)
print(response.text)
 ```

#### 3.7.2 解决方案

> 为了在代码中能够正常请求，我们使用 verify=False 参数，此时requests模块发送请求将不做CA证书验证：verify参数能够忽略CA证书的认证

```python
import requests

url = 'https://sam.huat.edu.cn:8443/selfservice/'

response = requests.get(url, verify=False)

print(response.text)
```

### 4. requests模块发送POST请求

> 注册，登录，传输大文本内容等情况下需要发送POST请求

#### 4.1 requests发送POST请求的方法

1.实现方法

* response = requests.post(url, data)
* data参数接收一个字典
* requests模块发送POST请求函数的其它参数和发送GET请求的参数完全一致

2.post数据来源

* 预设值 （抓包比较不变值）
* 输入值 （抓包比较根据自身变化值）
* 预设值-静态文件 （需要提前从html中获取（正则提取），要经常抓包）
* 预设值-发请求 （需要对指定地址发送请求，要经常抓包）
* 在客户端生成  （分析js，模拟生成数据，最难）

例子如下：

```python
import requests
import json


class King:
    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.key = word
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
        }
        self.data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }
    
    def get_data(self):
        # 发送一个post请求，data为请求体字典
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content
    
    def parse_data(self, data):
        # loads方法将json字符串转换成python字典
        dict_data = json.loads(data)
        try:
            return dict_data['content']['out']
        except:
            return dict_data['content']['word_mean'][0]
    
    def run(self):
        response = self.get_data()
        print(self.parse_data(response))


if __name__ == "__main__":
    word = input("请输入要翻译的词语：")
    king = King(word)
    king.run()
```

### 5. 利用requests.session进行状态保持

* 作用
  * 自动处理cookie

* 使用场景
  * 连续多次请求

* 使用方法

```python
import requests

session = requests.session() # 实例化session对象
response = session.get(url, headers, ...)
response = session.post(url, data, ...)
```