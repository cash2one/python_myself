# -*- coding:utf-8 -*-
# 重要
import matplotlib
matplotlib.use('Agg')

import numpy as np
from matplotlib import pyplot

# x = np.linspace(-4, 4, 30)
# y = np.sin(x)
# pyplot.plot(x, y, '--*b')

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)
pyplot.plot(x, c, color="blue", linewidth=2.5, linestyle="-", label="cosine")  #label用于标签显示问题
pyplot.plot(x, s, color="red",  linewidth=2.5, linestyle="-", label="sine")
print pyplot.show()  # 显示图片

pyplot.savefig("examples.jpg") # 保存图片


# # -*- coding: utf-8 -*-
# import numpy as np
#
# import matplotlib
# matplotlib.use('Agg')
# #  no display name and no $DISPLAY environment variable  上面两行
#
# # from matplotlib.pyplot import plot, savefig
# from matplotlib import pyplot
#
# x = np.linspace(-4, 4, 30)
# y = np.sin(x)
#
# pyplot.plot(x, y, '--*b')
# pyplot.show()  # 显示图片
# pyplot.savefig('MyFig.jpg')