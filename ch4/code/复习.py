# coding=utf-8
#1.数据的分类
    #1.结构化
    #2.非结构化

#2.json的用法
    #1.josn.loads json.dumps(python_obj,ensure_ascii=Fasle,indent=2)
    #2.json.load  json.dump

#3.正则表达式
    #1.re   re.split  re.findall() re.sub(r"","_",str) re.compile
    #2.  .(re.S\re.DOTALL)  \[ \. \*  + * ?

#4.原始字符串r
    # 忽视python中的特殊符号,\n,\t,带匹配的字符串是什么样子的,我们的正则就写什么样子的,加上r就可以

#5.xpath语法
    #1. //div
    #2. //div[@id='']   //div[contains(@id,'i')]
    #3. /a/@href  a/text()   //a//text()  //a[text()='下一页']

#6.lxml使用
    #序列化html_str 帮助自动补全,但是可能会出现问题, etree.tostring(element)
    #from lxml import etree
    #element = etree.HTML(response.content)
    # element = etree.HTML(response.content.decode())
    #element.xpath("")
    #分组:让其一一对应
