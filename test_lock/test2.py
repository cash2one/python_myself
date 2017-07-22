# -*- coding: utf-8 -*-

from threading import Thread
import time

def test_thread():
    print time.time()

threads = list()
for index in xrange(1, 5):
    threads.append(Thread(target=test_thread))

for thread in threads:
    thread.start()
