# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# 导入模板类
from Sun.items import SunItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    # 修改允许的域名
    allowed_domains = ['wz.sun0769.com']
    # 修改起始的url为目标url
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    # 详细页面的链接
    # 'html/question/\d+/\d+.shtml'
    'ndex.php/question/questionType?type=4&page=30'
    rules = (
        # 提取详细页面的url
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
        # 获取下一页url
        Rule(LinkExtractor(allow=r'questionType'), follow=True),
    )

    def parse_item(self, response):
        # 创建item用于存放数据
        item = SunItem()

        # 解析数据
        # 获取url
        item['detail_url'] = response.url
        # 获取id
        item['id'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract_first().split(':')[-1]
        # 获取标题
        item['title'] = response.xpath('/html/head/title/text()').extract_first().split('_')[0]


        # 获取内容
        content = ''.join(response.xpath('/html/body/div[6]/div/div[2]/div[1]/text()').extract())
        if  content.strip() == '':
            content = ''.join(response.xpath('//div[@class="contentext"]/text()').extract())
        item['content'] = content

        # print item['title']
        # 将数据返回给引擎
        yield item
