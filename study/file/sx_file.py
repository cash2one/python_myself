# -*- coding: utf8 -*-

import os
# filedir = "D:/regular/save_python_screenshot/2017-01-23/11/aa"
# print filedir
# os.mkdir(r"%s" % filedir)
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

mkpath = "D:/regular/save_python_screenshot/2017-01-23/1221/h哈哈试试hd".encode("gbk")
mkdir(mkpath)

