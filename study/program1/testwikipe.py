# coding: utf-8
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
request = urllib2.Request("http://www.zhaopin.com/", data=None, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari / 537.36'})
html = urlopen("http://www.zhaopin.com/")
