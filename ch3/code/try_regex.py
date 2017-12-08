# coding=utf-8
import re

a = "a\nb."

# print(re.findall("a.*b",a,re.S))
# print(re.findall("a.*b\.",a,re.S)) #转义符号\的使用

#正则表达或的用法
a= "abce_afce_adce"
# print(re.findall("abce|afce|adce",a))

#re.compile的使用
# p = re.compile(".+?",re.S)
# print(p.findall("chuanzhi"))

#re.sub的使用
# a = "chuan1zhi2"
# print(re.sub(r"\d","_",a))
# p = re.compile("\d")
# print(p.sub("_",a))

#原始字符串r
a = "a\nb"
print(len(a))
print(a)
print("*"*10)
b = r"a\nb"
print(b,len(b))