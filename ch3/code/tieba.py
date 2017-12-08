# coding=utf-8
import requests
from retrying import retry
from lxml import etree


class TiebaSPider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}".format(self.tieba_name)
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    @retry(stop_max_attempt_number=3)
    def _parse_url(self,url):
        print("now parsing:",url)
        response = requests.get(url, headers=self.headers, timeout=5)
        assert response.status_code == 200
        return etree.HTML(response.content)

    def parse_url(self, url):
        try:
            html = self._parse_url(url)
        except Exception as e:
            print(e)
            html = None
        return html

    def get_content_list(self, html):
        div_list = html.xpath("//div[contains(@class,'i')]")
        content_list = []
        for div in div_list:
            content = {}
            content["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None
            content["href"] = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/" + div.xpath("./a/@href")[0] \
                if len(div.xpath("./a/@href")) > 0 else None
            content_list.append(content)
        next_url = html.xpath("//a[text()='下一页']/@href")
        if len(next_url) > 0:
            next_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/" + next_url[0]
        else:
            next_url = None
        return content_list, next_url

    def get_img_list(self, html):
        img_list = html.xpath("//img[@class='BDE_Image']/@src")
        return img_list

    def save_coentent(self, content):
        print(content)

    def run(self):
        # 1.start_url
        next_url = self.start_url
        # 2.发送请求,获取响应
        while next_url is not None:
            html = self.parse_url(next_url)
            # 3.提取帖子的标题,url地址,下一页的url
            if html is not None:
                content_list, next_url = self.get_content_list(html)
                # 4.发送关于帖子的url的请求,获取响应
                for content in content_list:
                    detail_url = content["href"]
                    detail_html = self.parse_url(detail_url)
                    # 5.提取图片地址,item组装完成
                    content["img_list"] = self.get_img_list(detail_html)
                    # 5.1保存
                    self.save_coentent(content)
                    # 6.发送下一页的url请求,循环


if __name__ == '__main__':
    tieba_spdier = TiebaSPider("萌妹子")
    tieba_spdier.run()
