# -*- coding: utf-8 -*-

file_name = "../picture/test.png"
file_list = list()
file_list.append("../picture/test.png")
# file_list.append("../picture/btemp2.png")

# 图片转成jpg格式

# from __future__ import print_function
import os, sys
from PIL import Image

#
# for infile in file_list:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print("cannot convert", infile)

# 创建缩略图

# from __future__ import print_function
# import os, sys
# from PIL import Image
#
# size = (128, 128)
#
# for infile in file_list:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             im = Image.open(infile)
#             im.thumbnail(size)
#             im.save(outfile, "JPEG")
#         except IOError:
#             print("cannot create thumbnail for", infile)


im = Image.open(file_name)
box = im.copy() #直接复制图像
box = (100, 100, 400, 400)
region = im.crop(box)
print region.size
region.show()