#coding=utf-8
import requests
from retrying import retry
from lxml import etree
import json
from queue import Queue
import threading

class QiuBai:
    def __init__(self):
        self.temp_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    def get_url_list(self):#获取url列表
        # url_list = [self.temp_url.format(i) for i in range(1,14)]
        # return url_list
        for i in range(1,14):
            self.url_queue.put(self.temp_url.format(i))

    @retry(stop_max_attempt_number=3)
    def _parse_url(self,url): #发送请求,获取响应
        print("now parsing:",url)
        response = requests.get(url,headers=self.headers,timeout=5)
        assert response.status_code == 200
        return etree.HTML(response.content)

    def parse_url(self): #不捉异常
        while True:
            url = self.url_queue.get()
            try:
                html = self._parse_url(url)
            except Exception as e:
                print(e)
                html = None
            self.html_queue.put(html)
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html = self.html_queue.get()
            if html is not None:
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
                self.content_list_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self): #保存
        while True:
            content_list = self.content_list_queue.get()
            with open("qiubai.json","a",encoding="utf-8") as f:
                for content in content_list:
                    f.write(json.dumps(content,ensure_ascii=False,indent=2))
                    f.write("\n")
            print("save success")
            self.content_list_queue.task_done()

    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list) #处理url的子线程
        thread_list.append(t_url)
        #2.遍历,发送请求,获取响应
        for i in range(4):
            t_parse = threading.Thread(target=self.parse_url) #发送请求的子线程
            thread_list.append(t_parse)
        for i in range(2):
            t_content_list = threading.Thread(target=self.get_content_list) #提取数据的子线程
            thread_list.append(t_content_list)
        #4.保存
        t_save = threading.Thread(target=self.save_content_list) #保存数据的子线程
        thread_list.append(t_save)

        #启动
        for t in thread_list:
            t.setDaemon(True) #设置为守护线程,主线程结束,子线程结束
            t.start()

        for q in [self.url_queue,self.html_queue,self.content_list_queue]:
            q.join() #让主线程等待队列任务

if __name__ == '__main__':
    qiubai_spider = QiuBai()
    qiubai_spider.run()