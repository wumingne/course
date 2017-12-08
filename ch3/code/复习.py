# coding=utf-8
#1.如何发送post请求
# requests.post(url,data)

#2.如何使用代理
#proxies = {"http":"http://....:***"}

#reqeusts.get(url,proxies=proxies)

#3.如何模拟登录
    #1. session = requests.session()
        #session.get(url...)
    #2. #1. headers ={"cookie":"".....}
         #2.cookies = {"name":"value"}
         # requests.get(url,cookies=cookies)
    #3. 分析js