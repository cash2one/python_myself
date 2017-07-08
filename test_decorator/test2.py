# -*- coding: utf-8 -*-

import traceback

def dec(func):
    def in_dec(*args):
        # print func.
        for arg in args:
            if isinstance(arg, dict):
                print "dict:",arg["url"]
        sx = func(*args)
        return sx
    return in_dec

# def dec(func):
#     def in_dec(*args):
#         for arg in args:
#             if isinstance(arg, dict):
#                 print "dict:",arg["url"]
#         sx = func(*args)
#         return sx
#     return in_dec

@dec
def print_my(*args):
    for arg in args:
        print arg

sx_dict = {"test1": 1, "test2": "djd", "url": "baidu"}

# sx_dict = "hdhhd"
print_my(sx_dict)


# def my(*args):
#     print "haha"
#
# my()
