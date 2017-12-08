# coding=utf-8
import re
import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
}
url = "http://www.renren.com/327550029/profile"
cookie="anonymid=j3jxk555-nrn0wh; _r01_=1; depovince=BJ; _ga=GA1.2.1274811859.1497951251; _gid=GA1.2.1509487013.1502546781; JSESSIONID=abc4Op8Hm2wMjgpm6vz3v; ch_id=10016; wp_fold=0; jebecookies=fde7f749-5408-4b9e-a488-1f8a641504ca|||||; ick_login=9f2a9744-0100-47ca-98ea-03c3743a580f; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=66978036668cd005f2ff1b60b15b90149; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=ed52a6e2bb40762eaab0edb387f4ab9f9; societyguester=ed52a6e2bb40762eaab0edb387f4ab9f9; id=327550029; xnsid=26924ebb; loginfrom=syshome"

temp_lsit = cookie.split("; ")
cookies = {i.split("=")[0]:i.split("=")[1] for i in temp_lsit}
print(cookies)

response = requests.get(url,headers=headers,cookies=cookies)

print(re.findall(r"毛兆军",response.content.decode()))

#1.cookie 过期时间比较久,常见于一些比较老的网站
