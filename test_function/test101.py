# -*- coding: utf-8 -*-
# listsx = ["djdsj", 1, 34, "djd"]
# print listsx.pop()
#
# listsx.append("11222")
# print listsx
#
# print listsx.pop()

from Queue import Queue

proxy_list = Queue()

for i in xrange(0, 3):
    proxy_list.put(i)

print proxy_list.get()

import datetime
print "time:{} 代理异常".format(datetime.datetime.now())

print "start_time:{};length:{}".format(datetime.datetime.now(), 2)