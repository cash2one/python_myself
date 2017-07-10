# -*- coding: utf8 -*-

# for i in xrange(1, 10):
#     print i

# d = {"a": 1, "b": 2}
# for k, v in d.iteritems():
#     print k, v
#
# sxlist = ['A', 'B', 'C']
# for i, value in enumerate(sxlist):
#     print i, value


# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回  作用一个参数
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#   reduce作用于 两个参数
# def f(x):
#      return x * x
#
# sx = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print sx
#
# sx_list = ("1", "2", "24", "3")
# print map(int, sx_list)

sx_list = "12243"

def fn(x, y):
    return x + y
print reduce(fn, map(int, sx_list))


# def change(x):
#     # str(x).lower()
#     return x.lower().capitalize()
# test_list = ["dffA", "DHdjd", "kdkdDkf22"]
# print map(change, test_list)
# print map(lower, test_list)


# filter()函数用于过滤序列。  过滤 可迭代类型中得知
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def not_empty(s):
    return s and s.strip()

temp = ["sd", "", None, "djd"]
print filter(not_empty, temp)

# sorted 排序
sx_temp = [23, 45, 12, 99]
print sorted(sx_temp)

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted(sx_temp, reversed_cmp)

