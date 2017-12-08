#coding=utf-8
from parse import parse_url
import json

class NeiHan:
    def __init__(self):
        self.start_url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web"
        self.next_url_temp = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"

    def get_content_list(self,json_str): #提取数据和max_time
        content_dict = json.loads(json_str)
        temp_data = content_dict["data"]["data"]
        content_list = [[i["group"]["share_url"],i["group"]["text"]] for i in temp_data]
        max_time = content_dict["data"]["max_time"]
        has_more = content_dict["data"]["has_more"]
        return content_list,max_time,has_more

    def save_content_list(self,content_list): #保存
        with open("neihan.txt","a") as f:
            for content in content_list:
                print(content)
                f.write(content[0])
                f.write("\n")
                f.write(content[1])
                f.write("\n")

    def run(self):
        has_more = True
        next_url = self.start_url
        while has_more:
            #1.start_url
            #2.发送请求,获取响应
            json_str = parse_url(next_url)
            #3.提取数据,max_time
            content_list,max_time,has_more = self.get_content_list(json_str)
            #4.保存数据
            self.save_content_list(content_list)
            #5.下一页url,循环,has_more为false
            next_url = self.next_url_temp.format(max_time)


if __name__ == '__main__':
    neihan = NeiHan()
    neihan.run()