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
class test():

    def test(self):
        # baixing.com
        request = urllib2.Request("http://bj.lianjia.com/chengjiao/bp1850ep1860/", data=None, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari / 537.36'})
        #
        redirect_handler = UnRedirectHandler()
        # redirect_handler = redirect_handler
        # opener = urllib2.build_opener(redirect_handler)
        opener = urllib2.build_opener()

        try:
            response = opener.open(request, timeout=5)
            # print response
            print response.geturl()
            # html = response.read()
            # print html
            # print "到达"
        except HTTPError as e:
            #404  直接这边
            # print HTTPError.code
            print "404"
            print e.code
            # HTTPError.code
            print e
        except URLError as e:
            print "error"
            print e.reason
            # print URLError.reason
            #网络断开 走这边

# import urllib2.request as ur
#
# filehandler = ur.urlopen ('http://www.google.com')
# for line in filehandler:
#     print(line.strip())
class UnRedirectHandler(urllib2.HTTPRedirectHandler):

    def __init__(self):
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        # print code
        # print msg
        if 'location' in headers:
            newurl = headers.getheaders('location')[0]
            print 'header location:'+newurl
            return newurl
        pass

def Main():
    spider = test()
    spider.test();

    # if sys.argv[1]=='test':
	#    spider.test()
    # else:
    # print ('pc抓取程序开始启动...')
    # self.log.info('shjashsa')
    # spider.run(5, 50, 100, 20, 600, 600, 600, 600, True)
    # spider.run(5, 1, 1, 1, 600, 6000, 6000, 6000, True)
    # spider = EngineBasicSourceSpider()

if __name__ == '__main__':
    Main()