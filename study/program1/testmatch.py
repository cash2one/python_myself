# -*- coding: utf8 -*-
import re

# string1 = 'python'
# string2 = '012345'
# ma1 = re.match(r'.', string1)
# # print ma1
# print ma1.group()
#
# ma2 = re.match(r'.', string2)
# print ma2.group()
#
# ma = re.match(r'[p]',string1)
# print ma.group()#匹配出p
#
# ma = re.match(r'[a-z]',string1)#匹配a到z之间的字符
# print ma.group()#p
#
# ma = re.match(r'[0-9]',string2)#匹配0到9之间的字符
# print ma.group()#0
#
# ma = re.match(r'[a-zA-Z0-9]',string1)#a-z、A-Z和0-9可组合使用
# print ma.group()#p
#
# string4 = '[];;:'
# ma1 = re.match(r'\D',string4)#匹配非数字
# ma2 = re.match(r'\d',string2)#匹配数字
# print ma1.group()#[
# print ma2.group()#0

# ma = re.match(r'[a-z][a-z]*',string1)#小写字母开头，后接0个或者多个小写字母的字符串
# print ma.group()#python

# ma = re.match(r'[\w]{1,4}',string1)  #任意字母和数字出现1到4次
# print ma.group()#pyth

# ma = re.match(r'[\w][\w]*?', string1)#+最少匹配一次
# print ma.group() #py

# string3 = '''是是是哈哈哈'''
# ma = re.match(r'[\u4e00-\u9fa5]* ', string3)
# print ma.group()

# string5 = 'ali1bee@126.com'
# ma = re.search(r'[\w]', string5)
# print ma.group() #alibee

# string7 = '1,2,23,4'
# ma = re.findall(r'\d+', string7)
# print ma #['1', '2', '3', '4']

string8 = '6'#接字符串
# ma = re.sub(r'\d+','6',string8)
# print ma #6

# def addnumber(match) :  #接函数返回值
#     num = match.group()
#     num = int(num)+1
#     return str(num)
# ma = re.sub(r'\d+',addnumber,string8)
# print ma #6
#
# string7 = '''3,4,6,7'''
# ma = re.split(r',', string7)
# for m in ma:
#     print m
# print ma #['1','2','3','4']

# print "1"
# if  False:
#     print "dhdh"
# a = 1
# b = 2
# if a == 1 and b == 2:
#     print "cccccc"

# data = {"a": 1, "b": 2}
# data["c"] = 3
# print len(data)

# a  =  1000
# b =  6
# print a/b

str1 = u"aaassdd的角度讲 "
print isinstance(str1.encode("gbk"), str)