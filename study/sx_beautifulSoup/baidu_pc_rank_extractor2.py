# -*- coding: utf8 -*-
import sys
import re
import os
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, 'new_spider'))
# from spider.spider import SpiderExtractor
import datetime
from bs4 import BeautifulSoup

# from downloader.util_getRealAddress import GetReal_Address

reload(sys)
sys.setdefaultencoding('utf8')
class BaiduPcRankExtractor (object):

    def __init__(self):
        super(BaiduPcRankExtractor, self).__init__()


    '''
          获取pc排名数据
          response_status 0请求失败 1 请求成功
          百度关键词列表页数据
          '''

    def extractor_file_two(self, body, keyword=''):
        result = {}
        result['rank'] = []
        li = list()
        pos = body.find("</html>")
        if body.find('location.href.replace') >= 0 or body.find('id="wrap"') >= 0 or body.find(
                '<title>') < 0 or body.find(
            '页面不存在_百度搜索') >= 0 or body.find('id="container"') < 0 or pos < 0 or body.find('id="content_left"') < 0:
            result['response_status'] = 0
        else:
            try:
                # body = re.sub('\s', '', body)
                # # 获取标签内 内容
                # reshtml = re.findall(r'<divid="content_left">(.*?)<\/div><divstyle="clear:both;height:0;">', body)
                # if not reshtml:
                #     result['response_status'] = 0
                #     return li

                bsObj = BeautifulSoup(body, "lxml")
                containers = bsObj.find_all("div", {"class": "c-container"})
                if len(containers) > 0:
                    for container in containers:
                        toprank = None
                        title = ''
                        des = ''  # 描述
                        domain = ''
                        pos = 0
                        srcid = ''  # srcid
                        evaluate = ""  # 评价
                        realaddress = ""

                        toprank = container.attrs["id"]
                        title = container.find_all("h3")[0].get_text().replace(u"举报图片", "")
                        des_list = container.find_all("div", {"class": "c-abstract"})
                        if len(des_list) > 0:
                            des = des_list[0].get_text()
                        else:
                            des_list_two = container.find_all("div", {"class": "c-span18c-span-last"})
                            if len(des_list_two) > 0:
                                des = des_list_two[0].get_text()

                        evaluate_list = container.find_all("span", {"class": "c-pingjia"})
                        if len(evaluate_list) > 0:
                            evaluate = evaluate_list[0].get_text()

                        realaddress_list = container.find_all("a")
                        if len(realaddress_list) > 0:
                            realaddress = realaddress_list[0].attrs["href"]

                        print evaluate
                        print title
                        print toprank
                        print des
                        print realaddress

            except AttributeError as e:
                return None
            except Exception, e:
                print e

if __name__ == '__main__':
    f = open('polo.html', 'r')
    content = f.read()
    f.close()
    b = BaiduPcRankExtractor()
    l_s = b.extractor_file_two(content)
    # print l_s
    # sys.exit(1)
    # print l_s[0]['rank']
    # for l in l_s[0]['rank']:
    #     print '==========================='
    #     for r in l:
    #         print r



