# -*- coding:utf-8 -*-

def w1(func):
    def inner():
        print "验证"
        # 验证1
        # 验证2
        # 验证3
        return func()

    return inner


@w1
def f1():
    print 'f1'

f1()