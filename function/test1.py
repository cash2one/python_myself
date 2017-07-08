# -*- coding: utf8 -*-

import MySQLdb

# print "換行符"

d = {'Michael': 95, 'Tracy': 85}
print d.get("q", -1)
print d.get("Michael")
print d
d.pop('Michael')
print d

sx = [1, 2, 3]
s = set(sx)
s.add(4)
s.add("sss")
print s

help(abs)

