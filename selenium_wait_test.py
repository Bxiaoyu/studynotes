from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Chrome()

# 设置位置之后的所有元素定位操作都有最大等待时间10秒，在10秒内会定期进行元素定位，超过设置时间之后会报错
driver.implicitly_wait(10)

driver.get(url)

# print(driver.get_cookies())

# 将cookie存入一个字典
cookies = {data['name']:data['value'] for data in driver.get_cookies()}

print(cookies)