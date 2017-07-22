# -*- coding: utf-8 -*-

# sxdict = {"page": 1, "sx": 2}
#
# print sxdict.pop("page")
# print sxdict

# import json
#
# sxdict = {"sjsj":1, "djd":22}
# print type(json.dumps(sxdict))
#
# body = "dsds"
# print str(body).find("中关村在线") == -1


# from sys import getrefcount
#
# a = [1, 2, 3]
# print(getrefcount(a))
#
# b = [a, a]
# print(getrefcount(a))
# print(getrefcount(b))
#
# import gc
# print(gc.get_threshold())
# gc.collect() # 手动启动垃圾回收机制

# test = set()
# if test:
#     print "11"
# else:
#     print "22"
#
# for i in range(10):
#     print i

import hashlib
import MySQLdb

# def md5(s):
#     m = hashlib.md5()
#     m.update(s)
#     return m.hexdigest()
# st = md5(MySQLdb.escape_string("的设计的时候"))
# sv = ""
# for s in st:
#     sv += str(ord(s))
# print sv

import random


# sxlist = list(for i in xrange(10, 30))
# random.choice

import json
# str = """
#     Content-Type: text/html; charset=UTF-8
# Date: Fri, 21 Jul 2017 02:51:17 GMT
# Location: https://tieba.baidu.com/index.html
# P3p: CP=" OTI DSP COR IVA OUR IND COM "
# Server: Apache
# Set-Cookie: TIEBA_USERTYPE=b9c40c854d4080b28654293b; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com
# Set-Cookie: BAIDUID=A9ACC4FE9B4E5C4ACAE2D4C757E8411C:FG=1; expires=Sat, 21-Jul-18 02:51:17 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1
# Tracecode: 30772079930807191050072110
# Tracecode: 30772079930383042314072110
# X-Bd-Id: 6427618292900545967
# X-Bd-Oc: 16d95cfb2d7ba0f00006a58eab6d1ccb
# X-Bd-Ul: 752bcb03d01cc2fed9326fe0daa239d7
# X-Xss-Protection: 1; mode=block
# X_bd_https: 2
# Content-Length: 0
# Connection: close
#
# """
#
# print json.dumps(str)

import os

print os.path.dirname(os.path.abspath(__file__))

print os.path.join("D:\git_repository\python_myself", "test")

print os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_SourceSpider')
