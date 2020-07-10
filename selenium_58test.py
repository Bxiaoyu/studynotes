from selenium import webdriver

url = 'https://cd.58.com/chuzu/?PGTID=0d100000-0006-65b3-1372-e891dc949344&ClickID=2'

driver = webdriver.Chrome()

driver.get(url)

el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')

for el in el_list:
    print(el.text, el.get_attribute('href'))