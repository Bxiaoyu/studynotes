from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Chrome()

driver.get(url)

# 通过xpath进行元素定位
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# 通过css选择器进行元素定位
driver.find_elements_by_css_selector('#kw').send_keys('python')
# 通过name属性进行元素定位
driver.find_elements_by_name('wd').send_keys("python")
# 通过class属性值进行元素定位
driver.find_elements_by_class_name('s_ipt').send_keys('python')
# 通过链接文本进行元素定位
driver.find_elements_by_link_text('hao123').click()
# 取部分文本链接进行定位
driver.find_elements_by_partial_link_text('hao').click()
# 当目标元素在当前html中是唯一标签的时候或是众多定位出来的标签中的第一个时适用
driver.find_elements_by_tag_name('title')

driver.find_element_by_id('su').click()