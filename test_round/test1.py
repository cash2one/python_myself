# -*- coding: utf-8 -*-

# ta = [1, 2, 3]
# tb = [9, 8, 7]
# tc = ['a', 'b', 'c']
# for (a, b, c) in zip(ta, tb, tc):
#     print(a, b, c)

# S = 'abcdefghijk'
# for i in xrange(0, len(S), 2):
#     print S[i]

# ta = [1, 2, 3]
# tb = [9, 8, 7]
#
# # cluster
# zipped = zip(ta, tb)
# print(zipped)

# decompose
# na, nb = zip(*zipped)
# print(na, nb)

# def gen():
#     a = 100
#     yield a
#     a = a * 8
#     yield a
#     yield 1000

# def gen():
#     for i in range(4):
#         yield i
#
# for i in gen():
#     print i

# G = (x for x in range(4))
# for one in G:
#     print "G{}".format(one)

# print a.next()
#
# def gen():
#     yield 5
#     yield "Hello"
#     yield "World"
#     yield 4
# for i in gen():
#     print(i)


# def container(start, end):
#     while start < end:
#         yield start
#         start += 1
# c = container(0, 5)
# # print(type(c))
# # print(next(c))
# # next(c)
# for i in c:
#     print(i)


# def container(start, end):
#     while start < end:
#         yield start
#         start += 1
# c = container(0, 5)
# print(type(c))
# print(next(c))
# next(c)
# for i in c:
#     print(i)

# def container(start, end):
#     while start < end:
#         yield start
#         start += 1
# c = container(0, 5)
# print(type(c))
# print(next(c))
# next(c)
# for i in c:
#     print(i)
#
# print "ddsj"

# def func(a, b):
#     return a + b
#
# def test(f, a, b):
#     print 'test'
#     print f(a, b)
#
# test(func, 3, 5)

def add(*args):
    ret = 0
    for one in args:
        ret += one
    return ret

re1 = map(add, [1, 3, 5, 6])
print re1

# (lambda x, y: x+y)
re2 = map(add, [1, 2, 3], [6, 7, 9])
print re2

test_list = [1, 4, 6, 8, 4, 6]

sx_list = ["3232", "djus", "73"]
print ",".join(sx_list)

# print test_list.count(4)
#
# test_str = "hddhs2332"
# print test_str.isalnum()

# str.isalnum()        #返回：True， 如果所有的字符都是字母或数字
#
# str.isalpha()        #返回：True，如果所有的字符都是字母
#
# str.isdigit()        #返回：True，如果所有的字符都是数字
#
# str.istitle()        #返回：True，如果所有的词的首字母都是大写
#
# str.isspace()        #返回：True，如果所有的字符都是空格
#
# str.islower()        #返回：True，如果所有的字符都是小写字母
#
# str.isupper()        #返回：True，如果所有的字符都是大写字母

print("--------------------------------------------------------------")

import datetime
t = datetime.datetime(2012, 9, 3, 21, 30)
t_next = datetime.datetime(2012, 9, 5, 23, 30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)

print str(datetime.datetime.now() + datetime.timedelta(minutes=-2))

import os
os.chmod()