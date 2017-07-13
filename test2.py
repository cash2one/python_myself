# -*- coding: utf-8 -*-

# sxdict = {"page": 1, "sx": 2}
#
# print sxdict.pop("page")
# print sxdict

# import json
#
# sxdict = {"sjsj":1, "djd":22}
# print type(json.dumps(sxdict))
#
# body = "dsds"
# print str(body).find("中关村在线") == -1


from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = [a, a]
print(getrefcount(a))
print(getrefcount(b))

import gc
print(gc.get_threshold())
gc.collect() # 手动启动垃圾回收机制