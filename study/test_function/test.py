# -*- coding: utf8 -*-

# sxstr = "dhhdhdjs"
#
# # print str(sxstr)[0:16]
#
#
# print "dssssssss.com".endswith(".com")

# ds = None
# sx = """fhhfj||||"""
#
# print ds+sx
#
# lists = sx.split("||||")
# for data in lists:
#     if data!= "":
#         print 11
#         print data
# print len(lists)

# sxlist = [{"sx": "name", "age": "11"}]
# print sxlist
#
# print sxlist[0]["sx"]
#
#
# import re
#
# if re.search(u'百度手机助手', "百度手机助手22") > 0:
#     print "111"

import json

# strjson = """{ "sx": "name"}"""
#
# print type(strjson)
# print strjson
# sx = json.loads(strjson)
# print sx["sx"]

# strsx = '''{'fm':'','ensrcid':'www_normal','order':'1','mu':'http://m.zhaopin.com/'}'''
# print type(strsx)
# sx_1 = str(strsx).replace("\'", "\"")
#
# print sx_1

# print type(strsx)
# print

# sx_data = {"sx": "name"}
# jsonstr = json.dumps(sx_data)
#
# print jsonstr
# print type(jsonstr)
#
# jsonsx = json.loads(jsonstr)
# print jsonsx
# print type(jsonsx)



# sx = "招聘网"
#
# print sx.find("招聘")

import datetime
import time
time_now = datetime.datetime.today()
time.sleep(5)
time_now_end = datetime.datetime.today()

print (time_now_end-time_now).days

