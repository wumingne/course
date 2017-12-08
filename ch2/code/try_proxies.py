# coding=utf-8
import requests

url = "http://www.baidu.com"
proxies = {
    "http":"http://183.144.91.238:8998"
}

response = requests.get(url,proxies=proxies)
print(response.status_code)