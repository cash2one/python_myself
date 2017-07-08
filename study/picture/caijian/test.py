# -*- coding: utf8 -*-
# import Image
from PIL import ImageGrab, Image
import sys
import os.path
from  datetime import *
import random
import time

# IMAGE_BAKUP = "/few"
# _CONTENT_TYPES = { '.png': 'image/png', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.jpe': 'image/jpeg' }

_CONTENT_TYPES = {'image/png': '.png', 'image/gif': '.gif', 'image/jpeg': '.jpg', 'image/jpeg': '.jpeg'}

IMAGE_BAKUP = ''
# IMAGE_PATH = sys.arg[1]
# IMAGE_X1 = sys.arg[2]
# IMAGE_Y1 = sys.arg[3]
# IMAGE_X2 = sys.arg[4]
# IMAGE_Y2 = sys.arg[5]

IMAGE_PATH = "PC.png"
IMAGE_X1 = 10
IMAGE_Y1 = 200
IMAGE_X2 = 220
IMAGE_Y2 = 400

# x2 - x1 宽度
# y2 - y1 高度

im = Image.open("PC.png")  # 打开图片句柄
# im = Image.open(IMAGE_PATH)  # 打开图片句柄

box = (IMAGE_X1, IMAGE_Y1, IMAGE_X2, IMAGE_Y2)  # 设定裁剪区域

region = im.crop(box)  # 裁剪图片，并获取句柄region

region.save("33.png")

# IMAGE_BAKUP +
# region.save(datetime.now() + random.randint(0, 99), )  # 保存图片

# print int(time.time());
# print '%s%s-%s%s' % (IMAGE_BAKUP, int(time.time()), random.randint(0, 99), _CONTENT_TYPES[_CONTENT_TYPES])