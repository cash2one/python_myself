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

    # # 从调度中心取任务
    # def get_tasks(self):
    #     try:
    #         response = urllib2.urlopen(config.TASK_SCHEDULER_URL,
    #                                    data=urllib.urlencode({
    #                                        'type': config.FETCH_TYPE_HTML,
    #                                        'size': config.TASK_FETCH_SIZE,
    #                                        'client_id': self.id,
    #                                        'district_id': self.district_id
    #                                    }),
    #                                    timeout=config.TASK_FETCH_TIMEOUT)
    #         tasks = json.loads(response.read())
    #         if len(tasks) > 0:
    #             for task in tasks:
    #                 self.tasks.append(task)
    #     except Exception, e:
    #         pass
    #
    # # 返回结果给调度中心
    # def save_results(self, results, task_ids):
    #     request = urllib2.Request(config.TASK_SCHEDULER_URL,
    #                               data=urllib.urlencode({
    #                                   'type': config.FETCH_TYPE_HTML,
    #                                   'results': json.dumps(results),
    #                                   'task_ids': json.dumps(task_ids),
    #                                   'client_id': self.id
    #                               }))
    #     urllib2.urlopen(request)

    def send_post(self, sendurl, rankLists):
        try:
            response = urllib2.urlopen(sendurl,
                                       data=urllib.urlencode({
                                           'taskLists': rankLists,
                                           'saveport': "2"
                                      })
                                       )
            sx = response.read()
            print sx
        except Exception, e:
            pass

def main():
    downloader = AdslDownLoader()
    rankLists = """taskLists=[{"endtime":"2017-02-12 19:45:07","keywordid":"103","searchRegular":"1","starttime":"2017-02-10 19:45:07",
                        "searchDevice":"1","keyword":"11111ajjaj%E7%94%B5%E8%AF%9D%E8%B4%B9",
                        "addEditOrDelete":"1","searchType":"1","url":"hhh.baidu.comdjdj"}]"""

    sx = '''[{"endtime":"2017-02-12 19:45:07","keywordid":"1001","searchRegular":"1","starttime":"2017-02-10 19:45:07",
                        "searchDevice":"1","keyword":"11111ajjaj%E7%94%B5%E8%AF%9D%E8%B4%B9",
                        "addEditOrDelete":"1","searchType":"1","url":"hhh.baidu.comdjdj"}]'''

    # print urllib.urlencode({ 'taskLists': sx,
    #                                   })

    downloader.send_post("http://115.159.0.225:8080/InsideSystem_ws/baidurank/addTaskLists", sx)

if __name__ == '__main__':
    main()