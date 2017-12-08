# coding=utf-8
from selenium import webdriver
import time

class DouYu:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()  # 1.start_url
        # 2.发送请求
        self.driver.get(self.start_url)

    def get_content_list(self):  # 提取每页的数据,下一页的按钮
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        content_list = []
        for li in li_list:
            content = {}
            content["room_img"] = li.find_element_by_xpath(".//span[@class='imgbox']/img").get_attribute("src")
            content["room_title"] = li.find_element_by_xpath("./a").get_attribute('title')
            content["room_href"] = li.find_element_by_xpath("./a").get_attribute('href')
            content["room_cate"] = li.find_element_by_xpath(".//div[@class='mes']/div/span").text
            content["watch_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            print(content)
            content_list.append(content)
        next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        if len(next_url) > 0:
            next_url = next_url[0]
        else:
            next_url = None
        return content_list, next_url

    def save_content_list(self, content_list):  # 保存
        pass

    def __del__(self):
        self.driver.quit() #退出

    def run(self):
        # 1.start_url
        # 2.发送请求
        # 3.提取数据
        content_list, next_url = self.get_content_list()
        # 4.保存
        self.save_content_list(content_list)
        # 5.点击下一页的按钮,循环
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)
        # self.driver.quit()

if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()
