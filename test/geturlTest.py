# -*- coding: utf8 -*-
import os
import sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, 'new_spider'))
sys.path.append(os.path.join(PROJECT_PATH, 'store'))
sys.path.append(os.path.join(PROJECT_PATH, 'util'))

from spider.basespider_separate_deal_and_store import BaseSpiderSeparateDealAndStore
from downloader.html_local_downloader import HtmlLocalDownloader
from spider import config
from downloader.downloader import SpiderRequest
# from extractor.qidian.qidian_extractor import QidianChapterExtractor
# from store.qidian.qidian_book_store import QidianBookStore
# from store.qidian.qidian_category_store import QidianCategoryStore
# from store.qidian.qidian_sub_category_store import QidianSubCategoryStore
# from store.qidian.qidian_chapter_store import QidianChapterStore

from downloader.downloader import Downloader

from extractor.dianshang.dianshang_extractor import DianShangExtractor
from store.dianshang.dianshang_findhtml_store import DianShangFindhtmlStore

from store_mysql import StoreMysql
from util_log import UtilLogger
from util.util_useragent import UtilUseragent
from Queue import Queue
import random
import time
import datetime

from copy import copy
reload(sys)
sys.setdefaultencoding('utf8')


class geturlTest(BaseSpiderSeparateDealAndStore):
    """
    起点中文网爬虫
    """

    def __init__(self):
        super(geturlTest, self).__init__()
        self.user_agents = UtilUseragent.get('PC')
        self.sending_queue = Queue()
        # self.chapterExtractor = QidianChapterExtractor()
        # self.start_url = 'http://m.qidian.com/ajax/reader.ashx?bookid=%d&chapterid=%d&ajaxMethod=getchapterinfonew'
        self.log = UtilLogger('geturlTest',
                              os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_tmall_spider'))
        # 相差时间  删除数据库结果
        self.difsecond = 600

        self.difminute = 10
        #获取任务休眠时间
        self.sleepsecond = 60


    def get_user_password(self):
        # username ,password
        return  'sunxiang','sxspider'
        # return 'hemm', 'hmspider'


    def get_downloader(self):
        """
        设置下载器类型，默认为Downloader
        Return:
            SpiderDownloader
        """
        # return Downloader(set_mode='db', get_mode='db')
        return  HtmlLocalDownloader(set_mode='http', get_mode='http')

    def start_requests(self):
        try:
            self.log.info('抓取程序开始启动...')
            self.log.info('开始获取初始请求...')
            db = StoreMysql(**config.DIANSHANG_DB)

            start_time = datetime.datetime.now()
            # 一分钟执行一次
            results = list()
            # for row in rows:
            #     results.append({'id': row[0], 'url': row[1], 'headers': row[2]})
            #http://su.58.com/job.shtml
             # http://www.baidu.com/link?url=s2tdgwx355rosJ5lxZpXpY7B754Bp2UrRJnm9MytBrJ25P9w9ja7hvSzz6yTEVqv
             # http: // www.baidu.com / link?url = scC4tbm - 7
             # HIIlSuZHLgr18glaP6mPp0XipQYAykznVa
             # http://www.baidu.com/link?url=gsEpZxwaTdCuIojTr2iI0WOIyYrbXQoVWUB8Jq5xEZnC5Wd3K_j2npfjx7h68qhE
            # results.append({'id': 1, 'url': "http://www.baidu.com/link?url=x5aRO594-d2yGO8fzRl_6ompnamr_u4BSW9VQj1K-t7", 'headers':'11'})
            urls = list()
            # for result in results:
            #     urls.append({'url': result['url'], 'type': 2, 'id': result['id']})
            configs = { 'priority':2,'store_type': 1,  'redirect': 0 }

            request = SpiderRequest(headers={
                'User-Agent': random.choice(self.user_agents),

            }, config={'redirect': 0}, urls=[
                {'url': 'http://www.cnblogs.com/tonycody/p/3257611.html',
                 'type': 2}])
            self.sending_queue.put(request)
                # urls = list()


        except Exception, e:
            print e
            self.log.error('获取初始请求出错:%s' % str(e))

        time.sleep(self.sleepsecond)

    def deal_request_results(self, request, results):
        if results == 0:
            self.log.error('请求发送失败')
            self.sending_queue.put(request)
        else:
            self.sended_queue.put(request)


    def get_stores(self):
        stores = list()
        stores.append(DianShangFindhtmlStore())
        # stores.append(QidianCategoryStore())
        # stores.append(QidianSubCategoryStore())
        # stores.append(QidianChapterStore())
        return stores

    def deal_response_results(self, request, results, stores):
        if results == 0:
            self.log.error('获取结果失败')

        else:
                # 有结果为none
                urls = list()
                failed_urls = list()
                for u in request.urls:
                    url = u['url']
                    # id = u['id']
                    if url in results:
                        result = results[url]
                        print result['result']
                        print result['header']
                        if str(result['status']) == '2':
                            self.deal_chapter_response(u, result['result'],id)
                        elif str(result['status']) == '3':
                            self.log.error('抓取失败:%s' % url)
                            failed_urls.append(u)
                            # self.store_queue.put({'data': '-1', 'id': id})
                        else:
                            urls.append(u)
                    else:
                        self.log.error('url发送失败:%s' % url)
                        failed_urls.append(u)
                if len(urls) > 0:
                    request.urls = urls
                    self.sended_queue.put(request)
                if len(failed_urls) > 0:
                    new_request = copy(request)
                    new_request.urls = failed_urls
                    self.sending_queue.put(new_request)

    def deal_chapter_response(self, url, html, id):
        # chapters = self.chapterExtractor.extractor(html)
        # books = list()
        # categories = list()
        # sub_categories = list()
        # chs = list()
        # urls = list()
        # for chapter in chapters:
        #     if 'finished' in chapter and chapter['finished']:
        #         chs.append({'book_id': 0, 'chapter_id': url['chapter_id'], 'next_chapter_id': -1, 'status': 0})
        #         break
        #     if url['chapter_flag'] == 0:
        #         if 'book' in chapter:
        #             book = chapter['book']
        #             book['chapter_flag'] = 1
        #             books.append(book)
        #         if 'category' in chapter:
        #             category = chapter['category']
        #             categories.append(category)
        #         if 'sub_category' in chapter:
        #             sub_category = chapter['sub_category']
        #             sub_categories.append(sub_category)
        #     if 'chapters' in chapter:
        #         next_chapter_ids = list()
        #         chapter_ids = list()
        #         for ch in chapter['chapters']:
        #             chs.append(ch)
        #             if ch['next_chapter_id'] > 0:
        #                 next_chapter_ids.append(ch['next_chapter_id'])
        #             chapter_ids.append(ch['chapter_id'])
        #         for chapter_id in next_chapter_ids:
        #             if chapter_id not in chapter_ids:
        #                 urls.append({'url': self.start_url % (chs[0]['book_id'], chapter_id), 'type': 1,
        #                              'chapter_id': chapter_id, 'chapter_flag': 1})
        # self.store_queue.put( {'data': html, 'id': id})

        print  'end'
        # self.store_queue.put({'data': categories, 'type': 1, 'storeIndex': 1})
        # self.store_queue.put({'data': sub_categories, 'type': 1, 'storeIndex': 2})
        # self.store_queue.put({'data': chs, 'type': 3, 'storeIndex': 3})
        # if len(urls) > 0:
        #     request = SpiderRequest(headers={'User-Agent': random.choice(self.user_agents)}, urls=urls)
        #     self.sending_queue.put(request)

    def to_store_results(self, results, stores):
       # print len(results)
        stores[0].store(results)

    # def is_finish(self):
    #     """
    #     根据相关队列是否全都为空来判断任务处理结束
    #     """
        # return self.sending_queue.qsize() == -1 and self.sended_queue.qsize() == -1

def main():
    # d1 = datetime.datetime.now()
    # time.sleep(3)
    # d2 = datetime.datetime.now()
    # d = d2 - d1
    # print d.seconds
    spider = geturlTest()
    spider.run(1, 20, 20, 20, 600, 600, 600, 600, True)

if __name__ == '__main__':
    main()
