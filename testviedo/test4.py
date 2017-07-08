# -*- coding: utf-8 -*-
import requests
import urllib2


url = "http://data.bilibili.com/v/web/web_cm_event?callback=jQuery17209094251357471614_1492441791070&log_name=eventlog&page_ref=http%253A%252F%252Fwww.bilibili.com%252Fvideo%252Fav9495157%252F&resource_id=126&src_id=127&is_cm_loc=1&is_cm=1&event=show&ts=1492441838107&_=1492441838115"

# header = {"Referer": "http://www.bilibili.com/video/av9495157/",
#           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
#           "Host": "data.bilibili.com"}
#
# request = urllib2.Request(url, headers=header)
# video = urllib2.urlopen(request)
# string = "D:\\video\\2.mp4"
# fp = open(string, 'wb')
# print len(video.read())
# fp.write(video.read())

video = requests.get(url, timeout=10)
string = "D:\\video\\3.mp4"
fp = open(string, 'wb')
print len(video.content)
fp.write(video.content)