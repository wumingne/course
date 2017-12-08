# coding=utf-8
import requests

class TiebaSpider:

    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        temp_url = 'http://tieba.baidu.com/f?kw='+self.tieba_name+'&ie=utf-8&pn={}'
        self.url_list = [] #获取url列表
        for i in range(1000):
            self.url_list.append(temp_url.format(i*50))
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
        }

    def parse_url(self,url):#发送请求,获取响应
        print("now parsing",url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode() #获取html 字符串

    def save_html(self,html,page_num):#保存html字符串
        file_path = self.tieba_name+"_"+str(page_num)+".html"
        with open(file_path,"w") as f:
            f.write(html)
        print("保存成功")

    def run(self):
        #1.找到url规律,构造待请求的url列表
        for url in self.url_list:
            #2.拿到url,发送请求,获取响应
            #3.获取html 字符串
            html = self.parse_url(url)
            #4.保存
            page_num = self.url_list.index(url) + 1 #获取页码数
            self.save_html(html,page_num)

if __name__ == '__main__':
    tieba = TiebaSpider("猫")
    tieba.run()