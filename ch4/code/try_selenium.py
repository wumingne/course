#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.PhantomJS()
# driver.set_window_size(1920,1080) #设置框口大小
driver.maximize_window() #窗口最大化
driver.get("http://www.baidu.com")  #发送请求
# driver.save_screenshot("./baidu.png") #保存图片
driver.find_element_by_id("kw").send_keys("传智播客")  #找到元素,输入内容
driver.find_element_by_id("su").click()  #找到元素,点击
# time.sleep(5)

# print(driver.page_source) #网页源码
# print(driver.get_cookies())  #获取搜有cookie
# print("*"*50)
# cookie_temp = driver.get_cookies()
# cookies ={i["name"]:i["value"] for i in cookie_temp} #构造requests能够使用的cookies
# print(cookies)

# print(driver.current_url) #当前窗口的url

#find_element_by_xpath
time.sleep(3)
# href = driver.find_element_by_xpath('//*[@id="1"]/h3/a').get_attribute("href")
# text = driver.find_element_by_xpath('//*[@id="1"]/h3/a').text
# print(href)
# print(text)

#element和elements的区别
# temp = driver.find_elements_by_xpath("//div[contains(@class,'c-container')]")
# print(temp)
# for div in temp:
#     div.find_element_by_xpath("")

#by_link_text
href = driver.find_element_by_link_text("下一页>").get_attribute("href")
href = driver.find_element_by_partial_link_text("下一").get_attribute("href")

print(href)

driver.quit()