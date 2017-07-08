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
            # response = urllib2.urlopen(sendurl,
            #                            data=urllib.urlencode({
            #                                'taskLists': rankLists,
            #                                'saveport': "2"
            #                           })
            #                            )

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


    # send_configurl = "http://192.168.0.72:8000/Platform/receiveDate"
    #
    # imgdata = '''{"capture_red": "111", "screenshot_red":"ff"}'''
    # rankLists = """rankLists=[{"keywordid":"177","imgData":"%s","rank":2, "show_url":"www.baidu.com"}]""" % imgdata

    response = urllib.urlopen("www.baidu.com")
    sx = response.read()
    print str(sx)[0:20]


if __name__ == '__main__':
    main()