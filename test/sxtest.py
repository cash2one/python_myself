
# -*- coding: UTF-8 -*-
# print "sh大红色的"

# 文件名：test
# print "hello world!";print "ssddsds"
#
# counter = 100  # 整型变量
# miles = 1000.0  # 浮点数
# name = "john" # 字符串

# print counter
# 字符串
# s = 'lovexiaoxiaobai'
# print s[1:5]
# print s[-1]
#
# #python 列表
# list = [ 'xiaobai', 123, 2.22, 'john', 20.3]
# sxlist = [123, 'john']
#
# print min(list)
#
# print list
# print list[-2]      #从末尾开始 -1
# print list + sxlist
# print list[1:7]
#

# #python 元组  不能重复赋值 ，相当于只读列表
# tuple  = ('shsh', 231, 2.34)
# tup1 = ('physics', 'chemistry', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5, 6, 7 );
#
# print "tup1[0]: ", tup1[0]
# print "tup2[1:5]: ", tup2[1:5]
# print tuple[0]
# print tuple[1:3]

#python 字典 {}
# dict = {'Name': 'xiaobai', 'age': 7};
# print dict['age']


# dict = {}
# dict['one'] = 'xiaobai'
# dict[2] = 'this is two'
# tiny = {'name': 'john', 'code': 2323, 'dept': 'sale'}
# print dict['one']
# print dict[2]
# print tiny.keys()   #key 值列表
# print tiny.keys()[1]  #key 值某个位置

#数据类型转换   只需要将数据类型作为函数名
# s = '1'
# print int(s)+1
# print str(3)    #将对象 x 转换为字符串

#python  pass 不作任何操作   只是占位语句

#通过 del 删除单个或多个对象

# 可以删除 列表中 对象
# import types
# asx = 1
# if type(asx) is not types.IntType :
#     if asx == 1:
#         print asx

# a = 'ssdd'
# b = a * 2
# print 's' not in a

# print 'myname is %s and age is %d' % ('sx', 22)
# a = '''hahah "sjjsjs" ss'as' ss'''
# print a
# b = u'hello world'
# print b.encode(encoding='utf-8', errors='strict')
# b = 'sd3df22xx'
# print b.isalnum()

import time

# time = time.time()
# print time  #当前时间戳
# local = time.localtime(time.time())
# dt = time.strftime('%a  %A  %B  %x  %Y-%m-%d', time.localtime())
# print local
# print dt
# import calendar
# cal = calendar.month(2016, 1)
# print "以下输出2016年1月份的日历:"
# print cal

# def getnum(sd="sd"):
#     print sd
#
# print getnum('hanshu')

# def  printinfo(*sx):
#     "打印"
#     # print arg1
#     for var in sx:
#         print var
# list = [1, 'ss', 'sx']
# # printinfo(10)
# printinfo(list)

# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# import re
# phone = "2004-959-559 # 这1是一个国外电话号码"
# sx = re.compile('#.*$')
# # 删除字符串中的 Python注释
# num = sx.sub("", phone)
# print "电话号码是: ", num
#
# # 删除非数字(-)的字符串
# num = re.sub('\D', "", phone)
# print "电话号码是 : ", num
#
# num = re.sub('[0-9]', "", phone)
# print "电话号码是 : ", num

# print ('hei'*3)
# print ("hei bai\n"*7)

# a = 'ssas'
# print a != None

# a = 10
# b = 5
# if a > b:
#     print a> b

# tuple = [(1,2),(4,5,6)]
# print tuple[0][0]

# list = ["sxs", "11", "ey"]
# print list[0:2]

# demotuple = ("as", "vv", "bb")      #元祖不可修改
# print demotuple[0]

# s = "hello word it"
# print id(s)
# s = "chuanzhiboke"
# print id(s)
# print s

# print s
# s1 = "sdsdsd"
# s2 = "11111"
# print s1 + s2
# print s1*2
# print r'dsd\n'

# print "my name is %s and age is %d" % ("sx", 21)
#
# str = "wo name hahahah"
# print str.find("name", 0, 4)
# print str[3:]
# str.find("name")
# print str.index("sd")

# str = "hello world"
# print type(str)
# print str
# str.decode(encoding='utf-8')
# print type(str)
# print str

# import json
# js = json.loads('{"haha": "哈哈"}')
# # dict = json.dumps(js)
# print js
# print js["haha"]
# {"haha": "\u54c8\u54c8"}

# a = "sxsx哈啊哈哈"
# print a
# b = a.encode(encoding='utf-8', errors='strict')
# print b

# systr = 'maname 姓名namevbvbname'
# systr.i
# sx = systr.split('n')
# print sx
# for key in sx:
#     print key
# b = systr.replace('name', 'sx',1)
# print b
# print systr

# list1 = []
# list1.append("ss")
# print list1
# print len(list1)
# for list in list1:
#     print list
# print list1[0]
print "7272"

