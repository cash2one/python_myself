# -*- coding: utf-8 -*-

import numpy as np

arr = np.arange(10)

print arr

print arr[3:6]

arr_copy = arr[3:6].copy()

arr_copy[:]=24

print arr_copy

print arr