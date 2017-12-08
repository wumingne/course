# -*- coding: utf-8 -*-
import scrapy
# 导入item模板类
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取所有职位节点
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        print '-------',len(node_list)
        host = 'http://hr.tencent.com/'

        # 遍历节点列表，抽取数据
        for node in node_list:
            # 创建item实例
            item = TencentItem()
            # 抽取数据，放入到item对应字段中
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['url'] = host + node.xpath('./td[1]/a/@href').extract_first()
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['pub_time'] = node.xpath('./td[5]/text()').extract_first()



            # 创建一个请求，并发送
            yield scrapy.Request(item['url'],callback=self.parse_detail,meta={"itcast": item})


            # print item
            # for k,v in item.items():
            #     print k,v
            # print '&&&&&&&&&'
            # 将数据返回给引擎
            # yield item            #注销yield，因为直接返回的话，会被引擎交给管道，由管道保存

        # 获取下一页url
        next_url = host + response.xpath('//a[@id="next"]/@href').extract_first()
        # 创建新请求，并返回且引擎
        yield scrapy.Request(next_url,callback=self.parse)


    def parse_detail(self, response):
        # 获取到传递过来的item
        item = response.meta['itcast']

        # 提取详细要求
        item['duty'] = ''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        item['require'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())

        # 返回数据
        yield item