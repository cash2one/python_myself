# -*- coding:utf-8 -*-
'''
    多线程操作全局变量 使用互斥锁
    重点：声明一个全局互斥锁
'''
import threading
import time

counter = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter, mutex
        time.sleep(1)
        if mutex.acquire():
            print time.time()
            counter += 1
            print "I am %s, set counter:%s" % (self.name, counter)
            mutex.release()
            time.sleep(1)


if __name__ == "__main__":
    for i in range(0, 100):
        my_thread = MyThread()
        my_thread.start()