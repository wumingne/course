#coding=utf-8
from parse import parse_url
import re

class NeiHan:
    def __init__(self):
        self.start_url = "http://neihanshequ.com/"         #1.url
        self.pattern = re.compile(r"<a target=\"_blank\" class=\"image share_url\" href=\"(.*?)\".*?<p>(.*?)</p>",re.S)

    def get_content_list(self,html_str): #获取页面内容
        '''
        <a target="_blank" class="image share_url" href="http://neihanshequ.com/p66161465161/" data-group-id="66161465161" >

			<div class="upload-txt  no-mb">
				<h1 class="title">
				<p>上午去看牙，发现看牙的女医生长得挺漂亮，心想：现在女孩都喜欢有钱的，一定要找机会表现出来我的实力。 女医生问：牙坏了，拔么？ 故作紧张地问道：拔了牙的话影响我开宾利么？ 美女医生：不影响，就是吹牛逼的时候有点漏风！</p>
				</h1>
			</div>
        '''
        content_list = self.pattern.findall(html_str)
        return content_list

    def save_content_list(self,content_list): #保存
        with open("neihan.txt","a") as f:
            for content in content_list:
                print(content)
                f.write(content[0])
                f.write("\n")
                f.write(content[1])
                f.write("\n")

    def run(self):
        #1.url
        #2.发送请求,获取响应
        html_str = parse_url(self.start_url)
        #3.提取数据
        content_list = self.get_content_list(html_str)
        #4.保存
        self.save_content_list(content_list)

if __name__ == '__main__':
    neihan = NeiHan()
    neihan.run()