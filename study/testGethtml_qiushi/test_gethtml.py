# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

page = 2 # url = 'http://www.qiushibaike.com/hot/page/' + str(page)

# values = {'username': 'cqc', 'password': 'XXXX'}
# headers = {'User-Agent': user_agent}
# data = urllib.urlencode(values)

url = "http://www.qiushibaike.com/hot/page/%d/?s=4967552" % page
print url
try:
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    # print response.read()

    bsObj = BeautifulSoup(response, "lxml")
    articles = bsObj.find_all("div", {"class": "article block untagged mb15"})
    if articles:
        for article in articles:
            sx_span = article.find("span")
            print sx_span


    # content = response.read().decode('utf-8')
    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    # items = re.findall(pattern, content)
    # for item in items:
    #     print item[0], item[1], item[2], item[3], item[4]

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason