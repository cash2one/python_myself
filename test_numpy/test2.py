import pandas as np
from pandas import DataFrame

# data = p.read_table('aaa.txt', names=['key1', 'key2', 'time_h', 'count'])
# print data
#
# groupby_key2 = data.groupby([data['key2'], data['time_h']])
# count_key2 = groupby_key2.sum()
#
# print count_key2

import numpy as np

# arr = np.arange(1, 10).reshape(3, 3)
# print arr
#
# print arr[0][2]

# print np.arange(15)
# # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#
# print np.arange(15).reshape(3, 5)
#
# print np.linspace(1, 10, 20)


# a = np.ones((2, 2))
# b = np.eye(2)
# print a
# print b
# print np.vstack((a, b))
# print np.hstack((a, b))

a = np.array([[1, 0], [2, 3]])
print a

print a.transpose()
