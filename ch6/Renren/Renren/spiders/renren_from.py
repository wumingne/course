# -*- coding: utf-8 -*-
import scrapy


class RenrenFromSpider(scrapy.Spider):
    name = 'renren_from'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        data = {
            "email": "17173805860",
            "password": "1qaz@WSX3edc",
        }
        yield scrapy.FormRequest.from_response(response,formdata=data,callback=self.parse_after)

    def parse_after(self,response):
        with open('renren2.html','w')as f:
            f.write(response.body)
