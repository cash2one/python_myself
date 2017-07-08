# -*- coding: utf-8 -*-

from test_parse_html import parse_decorator

@parse_decorator(3)
def exception_my(a):
    print "11" + 1

sx = exception_my(1)
print sx