# -*- coding: utf-8 -*-

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         print b
#         a, b = b, a + b
#         n = n + 1
#
# print fab(5)

def mygenerator():
    print 'start...'
    yield 5

mygenerator()

mygenerator().next()