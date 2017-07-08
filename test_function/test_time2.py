# -*- coding: utf-8 -*-

import time

def timeit(func):
    def wrapper(*args):
        start = time.clock()
        ret = func(*args)
        end = time.clock()
        print "function_name:{0},used time:{1}".format(func.__name__, str(end - start))
        return ret
    return wrapper

@timeit
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

myfunc(1, 2)