# coding=utf-8
import requests
import re

session = requests.session()
#1.找到登录接口,找到post数据
url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

#2.发送请求,让cookie保存在session
session.post(url,data=post_data,headers=headers)

#3.发送关于个人主页的请求,获取响应,检查是否登录成功
response = session.get("http://www.renren.com/327550029/profile",headers=headers)
print(re.findall(r"毛兆军",response.content.decode()))