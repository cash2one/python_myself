# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

import numpy as np
import pylab as pl
x1 = [1, 2, 3, 4, 5]# Make x, y arrays for each graph
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 4, 6, 8]
y2 = [2, 4, 8, 12, 16]
pl.plot(x1, y1, 'r')# use pylab to plot x and y
pl.plot(x2, y2, 'g')
pl.title('测试. x')# give plot a title
pl.xlabel('x 周')# make axis labels
pl.ylabel('y 轴')
pl.xlim(0.0, 9.0)# set axis limits
pl.ylim(0.0, 30.)
pl.show()# show the plot on the screen
