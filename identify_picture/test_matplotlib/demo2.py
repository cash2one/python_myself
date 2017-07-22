# -*- coding: utf-8 -*-

# import matplotlib
# matplotlib.use('Agg')
#
# from matplotlib import pyplot
#
# import numpy as np
# import pylab as pl
# x = [1, 2, 3, 4, 5]# Make an array of x values
# y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
# pyplot.plot(x, y)# use pylab to plot x and y
# print pyplot.show()# show the plot on the screen
# pyplot.show("dome3.jpg")


import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]     # Make an array of x values
y = [1, 4, 9, 16, 25]   # Make an array of y values for each x value
# pl.plot(x, y)   # use pylab to plot x and y
# pl.plot(x, y, 'o')

pl.plot(x,y, '--')      # 虚线
# pl.plot(x, y, 'or')   # 红点

pl.show()    # show the plot on the screen
pl.savefig("sd.png")