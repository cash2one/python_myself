# -*- coding: utf-8 -*-
import numpy as np

import matplotlib
matplotlib.use('Agg')
#  no display name and no $DISPLAY environment variable  上面两行

from matplotlib.pyplot import plot, savefig

x = np.linspace(-4, 4, 30)
y = np.sin(x)

plot(x, y, '--*b')
savefig('MyFig.jpg')