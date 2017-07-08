# -*- coding: utf8 -*-
import urllib2

import urllib
import config
import json
import base64

import os
import sys

import time
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
import screenshot

class AdslDownLoader(object):

    def __init__(self):
        self.screenshot = screenshot.FindPicture()
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.id = ''
        # self.district_id = ''
        id_file = os.path.join(self.dir, 'machinenum.txt')
        if os.path.exists(id_file):
            with open(id_file) as f:
                lines = f.readlines()
                if len(lines) > 0:
                    self.id = lines[0].strip()
                    # print self.id
        self.tasks = []
        self.results = []

    # 从调度中心取任务
    def get_tasks(self):
        try:
            response = urllib2.urlopen(config.TASK_SCHEDULER_URL,
                                       data=urllib.urlencode({
                                           'type': config.FETCH_TYPE_SCREENSHOT,
                                           'size': config.TASK_FETCH_SIZE,
                                           'client_id': self.id
                                       }),
                                       timeout=config.TASK_FETCH_TIMEOUT)
            tasks = json.loads(response.read())
            if len(tasks) > 0:
                for task in tasks:
                    self.tasks.append(task)
        except Exception, e:
            pass

    # 返回结果给调度中心
    def save_results(self, results, task_ids):
        request = urllib2.Request(config.TASK_SCHEDULER_URL,
                                  data=urllib.urlencode({
                                      'type': config.FETCH_TYPE_SCREENSHOT,
                                      'results': json.dumps(results),
                                      'task_ids': json.dumps(task_ids),
                                      'client_id': self.id
                                  }))
        try:
            urllib2.urlopen(request)
        except Exception, e:
            pass

    @staticmethod
    def encoding(data):
        types = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'iso-8859-1']
        for t in types:
            try:
                return data.decode(t)
            except Exception, e:
                pass
        return None

    def run(self):
        self.get_tasks()
        results = list()
        task_ids = list()
        for task in self.tasks:
            task = json.loads(task)
            task_id = {"id": str(task["id"])}
            task_ids.append(task_id)
            result = {"id": str(task["id"]), "url": task["url"], "type": task["type"],
                      "store_type": task["store_type"], "status": "3", "result": "", "header": "",
                      "redirect_url": "", "code": 0}

            sxitem = json.loads(task["url"])
            resultdata = self.screenshot.picture_screenshot_html(sxitem["keyword"], sxitem["ckurl"],
                            int(sxitem["searchDevice"]), int(sxitem["spidertype"]), int(sxitem["searchPage"]), sxitem["returnType"])
            if resultdata:
                result["status"] = "2"
                result["result"] = base64.b64encode(str(resultdata))

            results.append(result)
            self.executeWindows("taskkill /f /im firefox.exe /t")
        if len(results) > 0:
            self.save_results(results, task_ids)

    def closeWarningFirefox(self):
        command = "taskkill /f /im firefox.exe /t"  # 在command = "这里填写要输入的命令"
        os.system(command)
        command = "taskkill /f /im WerFault.exe /t"  # 在command = "这里填写要输入的命令"
        os.system(command)

    def executeWindows(self, command):
        os.system(command)

    def get_body(self, header, body):
        if ('Content-Encoding' in header and header['Content-Encoding']) or \
                ('content-encoding' in header and header['content-encoding']):
            import gzip
            import StringIO
            d = StringIO.StringIO(body)
            gz = gzip.GzipFile(fileobj=d)
            body = gz.read()
            gz.close()
        body = self.encoding(body)
        return base64.b64encode(body)

def main():
    downloader = AdslDownLoader()
    downloader.run()
    # print "suzhou"

if __name__ == '__main__':
    main()
    # start_time = time.time()
    # while True:
    #     print datetime.today()
    #     main()
    #     time.sleep(1)
    #     # 切换ip
    #     if start_time + 300 < time.time():
    #         print "change ip"
    #         start_time = time.time()
    #         # "057114180549----875949"
    #         os.system("rasdial 宽带连接 /disconnect ")
    #         os.system("rasdial 宽带连接 057114180549 875949")
    #         time.sleep(10)

    # headers = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}
    # request = urllib2.Request("http://baixing.com", headers=headers)
    # opener = urllib2.build_opener(UnRedirectHandler())
    # response = opener.open(request, timeout=config.REQUEST_TIMEOUT)
    # header = response.info()
    # body = response.read()
    # print "1"