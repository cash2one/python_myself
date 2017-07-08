# coding: utf-8
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from bs4 import BeautifulSoup
# import BeautifulSoup
import re
def getTitle(f):
    # opener = urllib2.build_opener()
    # request = urllib2.Request("http://www.zhaopin.com/", data=None, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari / 537.36'})

    # try:
    #     # html = opener.open(request, timeout=10)
    #     # html = urlopen(url)
    # except HTTPError as e:
    #     print "404"
    #     return None
    # except URLError as e:
    #     # 网络断开 走这边
    #     print "error"
    #     print e
    try:
        bsObj = BeautifulSoup(f, "lxml")
        #获取标签内 内容
        title = bsObj.title.get_text()

        # print type(bsObj)
        # namelist = bsObj.find_all("div", {"class": "otherLogin"})
        # for name in namelist:
        #     alist = name.find_all("a")
        #     for a in alist:
        #         print a.get("href")

        # images = bsObj.findAll("img", {"src":re.compile("..\/ img\/gifts/img.*.jpg")})
        images = bsObj.findAll("img", {"src": re.compile("/img.*.jpg")})
        print len(images)
        for image in images:
            print(image["src"])

        # 页面中所有a 标签
        # alist = bsObj.find_all("a")
        # print len(alist)
        # for a in alist:
        #     print str(a)
        #     print type(str(a))
            # print "href" in a
    except AttributeError as e:
        return None
    return title

if __name__ == '__main__':
    f = open('1sx.html', 'r')
    content = f.read()
    f.close()
    title = getTitle(content)
    if title is None:
        print ("Title could not be found")
    else:
        print (title)