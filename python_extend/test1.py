# -*- coding:utf-8 -*-

import time
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    time.sleep(20)

if __name__ == "__main__":
    print 'start...'
    print u"3秒后,程序将结束...".encode("utf8")
    time.sleep(3)
    restart_program()
    print "2273"