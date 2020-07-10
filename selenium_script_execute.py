from selenium import webdriver

url = 'https://cd.lianjia.com/'

driver = webdriver.Chrome()

driver.get(url)

# 编写js代码，滚动条拖动
js = 'scrollTo(0, 1000)'
# 滚动条拖动
driver.execute_script(js)

el_button = driver.find_element_by_xpath('//*[@id="ershoufanglist"]/div/div[1]/p/a')
el_button.click()