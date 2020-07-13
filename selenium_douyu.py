#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
* @Author:     sky
* @date:       2020-07-13
* @version:    v1.0
* @description:selenium爬取斗鱼
"""
from selenium import webdriver


class Douyu:
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def parse_data(self):
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        data_list = []
        for room in room_list:
            temp = {}
            temp['title'] = self.driver.find_element_by_xpath('./a[1]/div[2]/div[1]/h3').text
            temp['type'] = self.driver.find_element_by_xpath('./a[1]/div[2]/div[1]/span').text
            temp['owner'] = self.driver.find_element_by_xpath('./a[1]/div[2]/div[2]/h2').text
            temp['num'] = self.driver.find_element_by_xpath('./a[1]/div[2]/div[2]/span').text
            temp['desc'] = self.driver.find_element_by_xpath('./a[1]/div[2]/span').text
            temp['image'] = self.driver.find_element_by_xpath('./a[1]/div[1]/div[1]/img').get_attribute('src')
            data_list.append(temp)
        return data_list
    
    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        self.driver.get(self.url)
        while True:
            # parse
            data_list = self.parse_data()
            # save
            self.save_data(data_list)
            # next
            try:
                el_next = self.driver.find_element_by_xpath('//*[contains(text(), "下一页")]')
                self.driver.execute_script('scrollTo(0, 100000)')
                el_next.click()
            except Exception as e:
                break

if __name__ == "__main__":
    dy = Douyu()
    dy.run()


