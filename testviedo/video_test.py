# -*- coding: utf-8 -*-

import urllib

folder = u"E:/video/"

# "https://d1.xia12345.com/down/201704/30/s85.mp4"

# with open("record.txt", "rb") as f:
#     list = f.readline()
#     f.close()
# num = 2
# for one in list:
#     filename = folder + "%d.mp4" % num
#     urllib.urlretrieve(one, filename)
#     num = num + 1
url = "https://d1.xia12345.com/2017/03/160222.mp4"
num = 1
filename = folder + "%d.mp4" % num
urllib.urlretrieve(url, filename)