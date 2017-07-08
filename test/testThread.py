#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time
import threading
from threading import Thread

# 为线程定义一个函数
def print_time( delay):
   count = 0
   # if count < 1:
   time.sleep(delay)
   count += 1
   print "%s" % (time.ctime(time.time()))

# 创建两个线程
try:
   # thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   # thread.start_new_thread( print_time, ("Thread-2", 4, ) )
   # thread.start( print_time, ("Thread-2", 1, ))
   # t = threading.Thread(target=print_time, args=(1))
   # t.start()

   t = Thread(target=print_time, args=(1,))
   t.start()
   print threading.activeCount()

   # threads = list()
   # threads.append(Thread(target=print_time, args=(1,)))
   # for thread in threads:
   #     thread.start()

except:
   print "Error: unable to start thread"

# while 1:
#    pass