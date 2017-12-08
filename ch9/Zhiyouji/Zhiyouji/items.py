# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # 企业名称
    name = scrapy.Field()
    # 浏览次数
    views = scrapy.Field()
    # 企业类型
    category = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 行业
    industry = scrapy.Field()
    # 公司简称
    short_name = scrapy.Field()
    # 公司简介
    desc = scrapy.Field()
    # 好评度
    praise = scrapy.Field()
    # 薪酬范围
    salary_range = scrapy.Field()
    # 产品列表
    products = scrapy.Field()
    # 融资信息
    financing_info = scrapy.Field()
    # 排名
    rank = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 网站
    website = scrapy.Field()
    # 联系方式
    contact = scrapy.Field()
    # qq
    qq = scrapy.Field()

