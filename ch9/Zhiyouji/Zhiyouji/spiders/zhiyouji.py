# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# 导入模板类
from Zhiyouji.items import ZhiyoujiItem
# ----1 导入类
from scrapy_redis.spiders import RedisCrawlSpider

# ----2 修改类的继承
# class ZhiyoujiSpider(CrawlSpider):
class ZhiyoujiSpider(RedisCrawlSpider):
    name = 'zhiyouji'

    # ----3
    # # 修改允许的域名
    allowed_domains = ['jobui.com']
    # # 修改起始的url
    # start_urls = ['http://www.jobui.com/cmp']

    # ----5 编写redis_key
    redis_key = 'crawlspider:start_urls'

    rules = (
        # 获取列表页面url
        Rule(LinkExtractor(allow=r'cmp\?n=\d+\#listInter'), follow=True),
        # 获取详情页面url
        Rule(LinkExtractor(allow=r'/company/\d+/$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print response.url,'----------'
        # 创建item
        item = ZhiyoujiItem()

        # 抽取数据
        item['name'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first()
        # 浏览次数
        item['views'] = response.xpath('//div[@class="grade cfix sbox"]/div[1]/text()').extract_first().split(u'人')[0].strip()
        # 企业类型
        try:
            item['category'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()').extract_first().split('/')[0]
        except:
            item['category'] = response.xpath('//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first().split('/')[0]
        # 规模
        try:
            item['number'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()').extract_first().split('/')[1]
        except:
            item['number'] = response.xpath('//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first().split('/')[1]
        # 行业
        item['industry'] = response.xpath('//dd[@class="comInd"]/a[1]/text()').extract_first()
        # 简称
        item['short_name'] = response.xpath('//dl[@class="j-edit hasVist dlli mb10"]/dd[3]/text()').extract_first()
        # 简介
        item['desc'] = ''.join(response.xpath('//*[@id="textShowMore"]/text()').extract())
        # 好评度
        item['praise'] = response.xpath('//div[@class="swf-contA"]/div/h3/text()').extract_first()
        # 薪酬范围
        item['salary_range'] = response.xpath('//div[@class="swf-contB"]/div/h3/text()').extract_first()
        # 产品列表
        item['products'] = response.xpath('//div[@class="mb5"]/a/text()').extract()


        # 获取融资信息
        data_list = []
        node_list = response.xpath('//div[5]/ul/li')
        for node in node_list:
            temp = {}
            temp['date'] = node.xpath('./span[1]/text()').extract_first()
            temp['status'] = node.xpath('./h3/text()').extract_first()
            temp['sum'] = node.xpath('./span[2]/text()').extract_first()
            temp['investors'] = node.xpath('./span[3]/text()').extract_first()
            # 放到列表中
            data_list.append(temp)

        item['financing_info'] = data_list

        # 排名信息
        data_list = []
        node_list = response.xpath('//div[@class="fs18 honor-box"]/div')
        for node in node_list:
            temp = {}
            key = node.xpath('./a/text()').extract_first()
            # 将名次转换为整形
            temp[key] = int(node.xpath('./span[2]/text()').extract_first())
            data_list.append(temp)
            # for k,v in temp.items():
            #     print k,v
        item['rank'] = data_list

        # 地址信息
        item['address'] = response.xpath('//dl[@class="dlli fs16"]/dd[1]/text()').extract_first()
        # 网站
        item['website'] = response.xpath('//dl[@class="dlli fs16"]/dd[2]/a/text()').extract_first()

        # 联系方式
        item['contact'] = response.xpath('//div[@class="j-shower1 dn"]/dd/text()').extract_first()
        # qq
        item['qq'] = response.xpath('//dd[@class="cfix"]/span/text()').extract_first()

        # for k,v in item.items():
        #     print k,v
        # print '####################'
        # 将数据返回
        yield item
