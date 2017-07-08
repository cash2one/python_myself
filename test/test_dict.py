# -*- coding:utf-8 -*-
# import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# a = {"大法好":"大师傅2",'SHSS':'HDHDS'}
# print "大师傅2" in a
# print "大法好" in a
# print len(a)
# print '大法好' in  a
#
# print a.keys()[0]

# for  key in a.keys():
#     print key
#     print a[key]

# kwh = {'wd': '发放贷款' , 'rn' : 50}
# url = 'https://www.baidu.com/s?'+urllib.urlencode(kwh)
# print url
#
# url2 = '发货后发的发的'
# print urllib.urlencode(url2)

string = u'https://www.baidu.com/s?wd=招聘'
d = string.encode('utf-8')
from urllib import urlencode
from urllib import quote
print quote("https://www.baidu.com/s?wd=御炼瓷&rn=50")
print urlencode({"l":u"中国","2":u"三"})
print len(string)
print len(d)
print d

# decode        encode
#
# types = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'iso-8859-1']
# for t in types:
#     try:
#         print string.decode(t)
#     except Exception, e:
#         pass


