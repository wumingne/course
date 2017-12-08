# coding=utf-8
import requests
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}

#发送请求
resposne = requests.get("http://36kr.com/",headers=headers)
#拿到html字符串
html_str = resposne.content.decode()

#通过正则表达式获取到结果,结果包含在response中,是一个json,这是正则表达式的常见用途
ret = re.findall(r'''<script>var props=({"activeInvestors\|investor".*?}})</script>''',html_str,re.S)
#findall返回一个列表,需要取第一个,也只有一个
ret = ret[0]
#通过保存到本地,观察报错的位置,发现其中比并不是只有json,所以需要继续操作
# with open("temp.json","w",encoding="utf-8") as f:
#     f.write(ret)

#不能直接loads,其中包含两个json字符串,后面的一个无用,所以替换成空字符串
ret = re.sub(r",locationnal=.*","",ret)

final_ret = json.loads(ret) #获取到结果
print(final_ret)
