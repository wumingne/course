#coding=utf-8
import requests
import json
import sys

class BaiduTrans:
    def __init__(self,query_string):
        #找到post url,post 数据
        self.query_string = query_string
        self.trans_url = "http://fanyi.baidu.com/v2transapi"
        self.post_data = {
            "from":"zh",
            "to":"en",
            "query":query_string,
            "simple_means_flag":3
        }
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
        }

    def parse_url(self):#发送翻译接口的请求
        response = requests.post(self.trans_url,headers=self.headers,data=self.post_data)
        return response.content.decode()

    def run(self):
        #1.找到post url,post 数据
        #2.发送请求,获取响应
        html_str = self.parse_url()
        #3.提取数据
        html_dict = json.loads(html_str)
        ret = html_dict["trans_result"]["data"][0]["dst"]
        print(self.query_string,"--->",ret)

if __name__ == '__main__':
    temp = sys.argv
    baidu_trans = BaiduTrans(temp[1])
    baidu_trans.run()