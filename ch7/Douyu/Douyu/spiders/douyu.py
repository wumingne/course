# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    # 修改允许的域名
    allowed_domains = ['capi.douyucdn.cn']
    # 保存 偏移量，接口
    offset = 0
    host = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset='
    # 修改起始的url列表
    start_urls = [host]

    def parse(self, response):
        # print response.body
        # 获取数据，转换为字典
        res = json.loads(response.body)
        # 获取数据列表
        data_list = res['data']
        for data in data_list:
            # 创建item
            item = DouyuItem()
            # 直接赋值
            item['nick_name'] = data['nickname']
            item['uid'] = data['owner_uid']
            item['image_link'] = data['vertical_src']
            item['city'] = data['anchor_city']


            # 返回数据
            yield item

        if len(data_list) != 0:
            # 拼接下一个url
            self.offset += 100
            next_url = self.host + str(self.offset)
            # 请求后续数据
            yield scrapy.Request(next_url,callback=self.parse)

