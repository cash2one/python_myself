# -*- coding: utf-8 -*-

from datetime import datetime
def log(func):
    def wrapper(*args, **kw):

        print 'call %s():' % func.__name__
        print "1122"
        return func(*args, **kw)
    return wrapper

@log
def now(a, b):
    print a+b
    print datetime.now()

now(1,2)