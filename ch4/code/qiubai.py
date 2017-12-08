#coding=utf-8
import requests
from retrying import retry
from lxml import etree
import json

class QiuBai:
    def __init__(self):
        self.temp_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}

    def get_url_list(self):#获取url列表
        url_list = [self.temp_url.format(i) for i in range(1,14)]
        return url_list

    @retry(stop_max_attempt_number=3)
    def _parse_url(self,url): #发送请求,获取响应
        print("now parsing:",url)
        response = requests.get(url,headers=self.headers,timeout=5)
        assert response.status_code == 200
        return etree.HTML(response.content)

    def parse_url(self,url): #不捉异常
        try:
            html = self._parse_url(url)
        except Exception as e:
            print(e)
            html = None
        return html

    def get_content_list(self,html):
        content_list = []
        div_list = html.xpath("//div[@id='content-left']/div") #包含div的element的列表
        for div in div_list:
            item = {}
            item["author_href"] = div.xpath("./div[@class='author clearfix']/a/@href")
            item["author_href"] = "https://www.qiushibaike.com"+item["author_href"][0] if len(item["author_href"])>0 else None
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else 0
            content_list.append(item)
        return content_list

    def save_content_list(self,content_list): #保存
        with open("qiubai.json","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
        print("save success")

    def run(self):
        #1.url_list
        url_list = self.get_url_list()
        #2.遍历,发送请求,获取响应
        for url in url_list:
            html = self.parse_url(url)
            # if html is not None:
                #3.提取数据
            content_list = self.get_content_list(html) if html is not None else []
            #4.保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai_spider = QiuBai()
    qiubai_spider.run()