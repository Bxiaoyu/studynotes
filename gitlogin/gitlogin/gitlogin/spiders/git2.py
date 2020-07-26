import scrapy
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


class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        # 将解析出来的数据存储到Formdata类变量中,这里可以用xpath，懒得改了
        Formdata.token = re.findall('name="authenticity_token" value="(.*?)"', response.content.decode())[0]
        Formdata.required_field_name = re.findall('<input class="form-control" type="text" name="(.*?)" hidden="hidden"', response.content.decode())[0]
        Formdata.time_stamp = re.findall('name="timestamp" value="(.*?)"', response.content.decode())[0]
        Formdata.timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)"', response.content.decode())[0]

        # 构造表单数据字典
        form_data = {}
        form_data['commit'] = Formdata.commit
        form_data['authenticity_token'] = Formdata.token
        form_data['ga_id'] = Formdata.ga_id
        form_data['login'] = 'xxxxx'
        form_data['password'] = 'xxxxxx'
        form_data['webauthn-support'] = Formdata.webauthn_support
        form_data['webauthn-iuvpaa-support'] = Formdata.webauthn_iuvpaa_support
        form_data['return_to'] = Formdata.return_to
        form_data[Formdata.required_field_name] = ''
        form_data['timestamp'] = Formdata.time_stamp
        form_data['imestamp_secret'] = Formdata.timestamp_secret
        print(form_data)

        # 针对登陆url发送post请求
        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.after_login,
            formdata=form_data
        )
    
    def after_login(self, response):
        yield scrapy.Request('http://github.com/exile-morganna', callback=self.check_login)
    
    def check_login(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())
