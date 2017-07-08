# -*- coding -*-

import random
import urllib2
import time

Baidu_spider = "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"

# 扫描本地IP或域名
domain_name = "http://127.0.0.1"

proxy_list = [  # 代理服务器，可能已经失效，换为自己的
    {'http': '117.28.254.130:8080'},
    {'http': '118.144.177.254:3128'},
    {'http': '113.118.211.152:9797'},
]

random_proxy = random.choice(proxy_list)  # 随机使用一个代理服务器
proxy_support = urllib2.ProxyHandler(random_proxy)
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

headers = {}
headers['User-Agent'] = Baidu_spider  # 蜘蛛的头部信息
# 玩蛇网 www.iplaypy.com

url = "http://www.iplaypy.com/crawler/multithreading-crawler-scanner.html"

request = urllib2.Request(url, headers=headers)
try:
    response = urllib2.urlopen(request)
    content = response.read()
    print content
    # if len(content):  # 内容不为空的情况下返回状态码、路径
    #     print "Status [%s]  - path: %s" % (response.code, path)

    response.close()
    time.sleep(1)  # 休息一会儿，防止速度过快连接数过大被封掉IP
except urllib2.HTTPError as e:
    # print e.code, path
    pass  # 异常处理，先暂时pass掉