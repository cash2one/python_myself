# -*- coding: utf-8 -*-

from pylab import *

from matplotlib import pyplot
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)
plot(x, c, color="blue", linewidth=2.5, linestyle="-", label="cosine")  #label用于标签显示问题
plot(x, s, color="red",  linewidth=2.5, linestyle="-", label="sine")
show()
pyplot.savefig("test.png")
