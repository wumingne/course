# -*- coding: utf-8 -*-
import scrapy
from Tianqi.items import TianqiItem

# ----1 导入scrapy_redis类
from scrapy_redis.spiders import RedisSpider
import time


# ----2 修改继承类
# class TainqiSpider(scrapy.Spider):
class TainqiSpider(RedisSpider):
    name = 'tainqi'

    # ----3 注销允许的域名和起始的URL列表
    # allowed_domains = ['tianqi.com']
    # # 修改起始的url
    # start_urls = ['http://lishi.tianqi.com/']

    # ----4 编写__init__,动态获取允许的域名
    def __init__(self,*args,**kwargs):
        # 获取域名
        domain = kwargs.pop('domain','')
        self.allowed_domains = filter(None,domain.split(','))
        # 调用父类初始化方法
        super(TainqiSpider,self).__init__(*args,**kwargs)

    # ----5 编写redis_key，用于从redis中获取起始url
    redis_key = "tianqi:start_urls"

    def parse(self, response):
        # 获取所有地区名列表
        area_list = response.xpath('//div[@id="tool_site"]/div[2]/ul/li/a/text()').extract()
        # 获取所有地区链接列表
        url_list = response.xpath('//div[@id="tool_site"]/div[2]/ul/li/a/@href').extract()
        # 遍历地区名和链接列表
        for area, url in zip(area_list,url_list)[:2]:
            # 对url做判断，看是否为#
            if url == "#":
                continue
            # 创建请求并发送
            yield scrapy.Request(url,callback=self.parse_area,meta={"area_1":area})


    def parse_area(self, response):
        # 接收meta传参
        area = response.meta['area_1']
        # print area,'*****'
        # 获取每一个月份url列表
        url_list = response.xpath('//*[@id="tool_site"]/div[2]/ul/li/a/@href').extract()

        # 遍历url列表
        for url in url_list:
            # 创建请求，并发送
            yield scrapy.Request(url,callback=self.parse_data,meta={"area_2":area})

    def parse_data(self, response):
        # print response.url,'888888888'

        # 接收meta传参
        area = response.meta['area_2']

        # 获取每一天的节点列表
        data_list = response.xpath('//*[@id="tool_site"]/div[@class="tqtongji2"]/ul')
        # print len(data_list),'*******',response.url

        # 遍历节点列表
        for data in data_list[1:]:
            # print '--------------'
            # 创建item实例
            item = TianqiItem()
            # 提取数据，存放到item中

            # 地区名
            item['area'] = area
            # 采集地址
            item['url'] = response.url
            # 时间戳
            item['timestamp'] = time.time()
            # 日期
            item['date'] = data.xpath('./li[1]/text()').extract_first()
            if item['date'] == None:
                item['date'] = data.xpath('./li[1]/a/text()').extract_first()

            item['max_t'] = data.xpath('./li[2]/text()').extract_first()
            item['min_t'] = data.xpath('./li[3]/text()').extract_first()
            item['weather'] = data.xpath('./li[4]/text()').extract_first()
            item['wind_direction'] = data.xpath('./li[5]/text()').extract_first()
            item['wind_power'] = data.xpath('./li[6]/text()').extract_first()

            # for k,v in item.items():
            #     print k,v
            # print '####################'

            # 返回数据
            yield item











