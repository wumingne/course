# coding=utf-8
#1.什么是爬虫
#模拟浏览器发送网络请求,获取响应

#2.爬虫的分类
#通用爬虫
#聚焦爬虫

#3.聚焦爬虫的流程
#url --->发送请求,获取响应 --->数据--->保存

#4.字符串的转化
#str encode bytes
#byte  decode str

#5.requests的使用
# response = requests.get(url,headers,params)
# response.text #response.encoding="utf-8"
# response.content.decode()
# response.request.headers
# response.request.url
