from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://cd.58.com/'

driver.get(url)

print(driver.current_url)
print(driver.current_window_handle)

# 定位并点击租房按钮
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

print(driver.current_url)
print(driver.current_window_handle)

driver.switch_to.window(driver.window_handles[-1])

el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')
print(len(el_list))