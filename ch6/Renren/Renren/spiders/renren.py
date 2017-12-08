# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        # 获取提交数据的url
        url = self.start_urls[0]
        # 构建传递的数据
        data = {
            "email":"17173805860",
            "password": "1qaz@WSX3edc",
        }
        #
        yield scrapy.FormRequest(url,callback=self.parse,formdata=data)



    def parse(self, response):
        with open('renren.html','w')as f:
            f.write(response.body)