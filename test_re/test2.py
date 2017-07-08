# -*- coding: utf-8 -*-

import re
str = '33'
ma = re.match(r'.*', str)
print ma.group()

ma = re.match(r'[A-Z][a-z]', 'Ass')
print ma.group()

ma = re.match(r'[_a-zA-Z]+[_\w]*', '_jddss')
print ma.group()

str2 = "11ddnnd22"
ma = re.match(r'11(.*?)22', str2)
print ma.group()

print re.findall(r'11(.*?)22', str2)[0]

print re.search(r'\d+', "jdjdj12344").group()

info = "aaa=123, ddj=89"
print re.findall(r'\d+', info)

re.sub()
