# -*- coding: utf-8 -*-

from PIL import Image
img1 = Image.open("../picture/test.png")
w, h = img1.size
print w, h

out = img1.resize((128, 128))
out = img1.rotate(90) # 逆时针角度表示

print out.size
out.show()

out = img1.transpose(Image.FLIP_LEFT_RIGHT)
out.show()

# 置换图像
# out = im.transpose(Image.FLIP_TOP_BOTTOM)
# out = im.transpose(Image.ROTATE_90)
# out = im.transpose(Image.ROTATE_180)
# out = im.transpose(Image.ROTATE_270)
# transpose()和象的rotate()没有性能差别。

# r, g, b = img1.split()
# im = Image.merge("RGB", (b, g, r))
# im.show()

# box = (100, 100, 400, 400)
# region = img1.crop(box)
# region.show()

# from PIL import ImageEnhance
#
# enh = ImageEnhance.Contrast(img1)
# enh.enhance(1.3).show("30% more contrast")



