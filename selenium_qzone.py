from selenium import webdriver


url = 'https://qzone.qq.com/'

driver = webdriver.Chrome()

driver.get(url)

# 遇到frame标签时，需要切换到此frame框架下才能进行框架内的其它操作
#driver.switch_to_frame('login_frame')
el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to_frame(el_frame)

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('QQ号')
driver.find_element_by_id('p').send_keys('密码')
driver.find_element_by_id('login_button').click()