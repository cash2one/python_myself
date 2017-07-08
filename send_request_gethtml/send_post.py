# -*- coding: utf8 -*-
import urllib2
# from redirect import UnRedirectHandler
import urllib
# import config
import json
import base64
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class AdslDownLoader(object):

    def __init__(self):
        pass

    def send_post(self, sendurl, rankLists):
        try:
            response = urllib2.urlopen(sendurl,
                            data=urllib.urlencode({
                                'taskLists': rankLists,
                                'saveport': "1"
                            }),
                            timeout=10)

            sx = response.read()
            print sx
        except Exception, e:
            pass


def main():
    downloader = AdslDownLoader()
    rankLists = """[{"endtime":"2017-02-12 19:45:07","keywordid":"103","searchRegular":"1","starttime":"2017-02-10 19:45:07",
                        "searchDevice":"1","keyword":"11111ajjaj%E7%94%B5%E8%AF%9D%E8%B4%B9",
                        "addEditOrDelete":"1","searchType":"2","returnType":"1111","targetKeywords":"djdj,sjsj"}]"""

    # url = "http://webtest.winndoo.com/RankTask/receiveData"

    # "url":"hhh.baidu.comdjdj",
    # sx = '''[{"endtime":"2017-02-12 19:45:07","keywordid":"100122","searchRegular":"1","starttime":"2017-02-10 19:45:07",
    #                     "searchDevice":"1","keyword":"招聘",
    #                     "addEditOrDelete":"1","searchType":"1","url":".zhaopin.com","returnType":"1111"}]'''
    #
    # # print urllib.urlencode({ 'taskLists': sx,
    # #                                   })
    #
    # # downloader.send_post("http://115.159.0.225:8080/InsideSystem_ws/baidurank/addTaskLists", sx)
    # downloader.send_post("http://localhost:8080/InsideSystem_ws/baidurank/addTaskLists", sx)

    # send_configurl = "http://webtest.winndoo.com/Platform/receiveDate"
    #
    imgdata = '''{"capture_red": "111", "screenshot_red":"ff", "capture": "", "screenshot":""}'''
    rankLists = """[{"keywordid":"177","imgData":"%s","rank":2, "show_url":"www.baidu.com"}]""" % imgdata
    # senditem = {"taskLists": rankLists}

    temp = """[{"keywordid": "111", "imgData": "", "rank": -2, "show_url": "", "real_address": ""}]"""

    # url = "http://115.159.0.225:8080/InsideSystem_ws/baidurank/addPulldownLists"
    # senditem = {"taskLists": rankLists, "saveport": "1"}

    url = "http://192.168.0.73:8000/RankTask/receiveData"
    # request = urllib2.Request(url, urllib.urlencode(senditem))
    # response = urllib2.urlopen(request)
    # sx = response.read()
    # print str(sx)[0:20]

    print temp
    print len(temp)
    try:
        request = urllib2.Request(url, data=urllib.urlencode({"rankLists": temp}))
        response = urllib2.urlopen(request, timeout=20)
        sx = response.read()
        print str(sx)[0:20]
    except Exception, e:
        print e

if __name__ == '__main__':
    main()