# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    name = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 数量
    number = scrapy.Field()
    # 地点
    address = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    pass
