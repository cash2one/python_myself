# -*- coding: utf-8 -*-

# from memory_profiler

from memory_profiler import profile
from memory_profiler import memory_usage

import time
# from guppy import hpy

@profile
def func2():
    c = [1] * (10 ** 6)
    return "b"

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    b = "11"
    # func2()
    return '11'

if __name__ == '__main__':
	my_func()