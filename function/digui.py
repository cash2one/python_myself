# -*- coding: utf-8 -*-

def func(arg1,arg2):
    if arg1 == 0:
        print arg1, arg2
    arg3 = arg1 + arg2
    print arg3
    func(arg2, arg3)

func(0,1)
