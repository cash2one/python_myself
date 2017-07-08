# coding: utf-8
import urllib2
from urllib2 import HTTPError

'''
    设置代理  http://175.146.228.178:8998    ip:port
'''
proxy = "http://175.146.228.178:8998"

# 创建一个ProxyHandler对象
# urllib2.Request
proxy_support = urllib2.ProxyHandler({'http': proxy})
# 创建一个opener对象
opener = urllib2.build_opener(proxy_support)
# 给request装载opener
urllib2.install_opener(opener)
# 打开一个url
try:
    r = urllib2.urlopen('http://115.159.148.162:8080/searchWebVersionOne/index.jsp', timeout=10)
    html = r.read()
    print html
    print len(html)
except HTTPError as e:
    print e

