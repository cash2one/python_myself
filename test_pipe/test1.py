# import multiprocessing as mul
#
# def f(x):
#     return x*2
#
# pool = mul.Pool(5)
# rel = pool.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(rel)

import multiprocessing
import time

def func(msg):
    for i in xrange(3):
        print msg
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=func, args=("hello", ))
    p.start()
    p.join()
    print "Sub-process done."