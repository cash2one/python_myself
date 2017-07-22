# -*- coding:utf-8 -*-
import numpy as np

import matplotlib
import pandas as pd
from pylab import *

matplotlib.use('Agg')
from matplotlib.pyplot import plot, savefig
from matplotlib import pyplot

from matplotlib.pyplot import savefig as sa


# df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
# df = df.cumsum()
# print df.plot()
# print show()
# sa("test2.jpg")

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)
plot(x, c, color="blue", linewidth=2.5, linestyle="-", label="cosine")  #label用于标签显示问题
plot(x, s, color="red",  linewidth=2.5, linestyle="-", label="sine")

# plot(x, y, '--*b')
# plt.show()
pyplot.savefig('test2.jpg')