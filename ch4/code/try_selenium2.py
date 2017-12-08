# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/f?kw=萌妹子&ie=utf-8&pn=0")
print(driver.find_element_by_partial_link_text("下一").text)
print(driver.find_element_by_link_text("下一页>").get_attribute("href"))
driver.close()