# coding: utf-8
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
request = urllib2.Request("http://www.zhaopin.com/",data=None, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari / 537.36'})
'''
   有网站  网站下面没有这个链接 返回 404   HTTPError
   没有网站     直接返回 URLError  和 网络断开一样
'''
try:
    html = opener.open(request, timeout=10)

    if html is None:
        print("URL is not found")
    else:
        bsObj = BeautifulSoup(html.read(), "lxml")

        # print bsObj.attrs("head")
        # print(bsObj.nonExistentTag)

        # 获取所有的该标签
        metas = bsObj.find_all(id= "top")
        for meta in metas:
            sx = meta.find_all(id= "top")
            print sx
            print meta
            # res = meta.attrs
            # try:
            #     print res["content"]
            # except Exception, e:
            #     print e

except HTTPError as e:
   # 404  直接这边
    print "404"
    print e
except URLError as e:
    #网络断开 走这边
    print "error"
    print e
# print bsObj

