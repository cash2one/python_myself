# -*- coding:utf-8 -*-
# 图片拼接练习
import PIL.Image as Image
import os, sys

mw = 375
ms = 667

msize = mw * ms

fpre = "s10100"
toImage = Image.new('RGBA', (mw, ms*2))

for y in range(0, 2):
    for x in range(0, 1):
        # print x,y
        # fname = "%s/%s_%s_%s.jpg" % (fpre, fpre, y, x)
        # print fname
        fname = "capture.png"
        fromImage = Image.open(fname, "r")
        toImage.paste(fromImage, (x * mw, y * mw))

toImage.save('44.jpg')