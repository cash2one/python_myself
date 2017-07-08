# -*- conding: utf-8 -*-

import re
import urllib2

request = urllib2.Request("http://www.imooc.com/course/list")
response = urllib2.urlopen(request, timeout=20)
r = response.read()
# print r

imglist = re.findall(r'http.+\.jpg', r)

print imglist


folder = "E:/img/"
for i, v in enumerate(imglist):
    with open(folder + "%d.jpg" % i, "wb") as f:
        f.write(urllib2.urlopen(v).read())

