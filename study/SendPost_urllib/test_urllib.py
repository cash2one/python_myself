# coding: utf8

import urllib
import urllib2

print "简单点"

import urllib2

# url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username': 'cqc', 'password': 'XXXX'}
# headers = {'User-Agent': user_agent}
# data = urllib.urlencode(values)
# request = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(request)
# page = response.read()


'''


headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }

Referer : 反盗链

'''


url = 'https://www.baidu.com/?tn=78040160_5_pg&ch=1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc', 'password': 'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
data = None
# , data, headers
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request, timeout=10)
page = response.read()
print page

# python
# import urllib2
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)


import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason