# coding=utf-8
import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)
print("*"*50)
#把cookiejar对象转化为字典
print(requests.utils.dict_from_cookiejar(response.cookies))
print("*"*50)
#把字典转化为cookiejar对象
print(requests.utils.cookiejar_from_dict({'BDORZ': '27315'}))