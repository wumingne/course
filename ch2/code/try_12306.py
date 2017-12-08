# coding=utf-8
import requests
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
url ="https://www.12306.cn/mormhweb/"
response = requests.get(url,headers=headers,verify=False)
print(response.status_code)