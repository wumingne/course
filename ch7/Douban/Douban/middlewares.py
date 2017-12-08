# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# 导入请求头列表
from settings import USER_AGENT_LIST
# 导入代理ip列表
from settings import PROXIES
# 导入随机模块
import random

import base64



class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 随机功能
# 一堆请求头



# 创建一个中间件类
class RandomUserAgent(object):

    # 编写对请求的操作
    def process_request(self, request, spider):
        # 随机获取一个用户头
        ua = random.choice(USER_AGENT_LIST)
        print ua,'*********'
        # 修改用户头
        request.headers['User-Agent'] = ua

# 创建一个代理ip中间件类
class RandomProxy(object):
    # 队请求进行操作
    def process_request(self, request, spider):
        # 随机获取一个代理
        proxy = random.choice(PROXIES)
        # 判断代理是否含有账号密码
        if proxy.has_key('user_passwd'):        # 有密码的情况
            # 对账号密码进行编码
            b64_user_pwd= base64.b64encode(proxy['user_passwd'])
            # 将编码之后的账号密码赋值给请求对应的值
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_user_pwd
            # 使用代理ip
            request.meta['proxy'] = 'http://' + proxy['ip_port']
        else:
            # 没有密码直接使用
            request.meta['proxy'] = 'http://' + proxy['ip_port']