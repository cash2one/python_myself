# -*- coding: UTF-8 -*-
# import requests
#
# res = requests.get("http://www.itcast.cn")
#
# savefile = open("itcast.html","w")
#
# savefile.write(res.content)
#
# savefile.close()

# sx = "shsh.,.\,.\,.sh,\.,"
# print sx.replace("\\", "")
#
# from datetime import datetime, timedelta
#
# sx = 300
# expire_time = str(datetime.now() + timedelta(seconds=-sx))
# print expire_time

# sx = ["1", "2", "3", "4"]
# # print tuple(sx)
#
# print ",".join(sx)

import urllib

url = "http://map.onegreen.net/中国县级区划地图.jpg"
urllib.urlretrieve(url, "E:/greenmap/1.jpg")