# -*- coding: utf-8 -*-

import MySQLdb

# 为了防止数据攻击
print MySQLdb.escape_string("'11'")

strtest = "ganxie"
if strtest.index("cc"):
    print "11"
else:
    print "22"