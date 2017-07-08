# coding: utf-8
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
# from urllib2
# import  ProxyHandler
# from urllib2.request import urlopen
# html = urllib2.urlopen("https://www.baidu.com/?tn=78040160_5_pg&ch=1")
# opener = urllib2.build_opener()

# opener.addheaders
#

# proxy=ProxyHandler({'http':'http://someproxy.com:8080'})
# auth=HTTPBasicAuthHandler()
# auth.add_password()
# opener=build_opener(auth,proxy)


request = urllib2.Request("http://bj.lianjia.com/chengjiao/bp1850ep1860/", data=None,
            headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari / 537.36'})

opener = urllib2.build_opener()
response = opener.open(request, timeout=5)
print response.geturl()
print response.read()
