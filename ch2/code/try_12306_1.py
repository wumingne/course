# coding=utf-8
import requests
from retrying import retry
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
proxies = {"https":"https://111.155.116.242:8123"}

#发送请求,获取响应
@retry(stop_max_attempt_number=3)  #函数执行3次,如果三次全部失败则失败,否则继续执行
def parse_url(url):
    print("*"*10)
    response = requests.get(url,headers=headers,timeout=3,proxies=proxies,verify=False)
    assert response.status_code == 200
    print("请求成功")

if __name__ == '__main__':
    url = "https://www.12306.cn/mormhweb/"
    parse_url(url)