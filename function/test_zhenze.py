# -*- coding: utf-8 -*-

import re

s = 'ABC\\-001'
sr = r'ABC\-001'  # 不考虑转义

test = "用户数入字符串"
if re.match(r"字符", test):
    print True
else:
    print False

# 字符串切片
print re.split(r"\s+", "a  b c  d")

test3 = "http:hhdhd://d"
print re.split(r"[\:\/]", test3)

print 22
print 22
print 22
print "解放22军金纺"
