# -*- coding: utf8 -*-

from PIL import Image
import matplotlib.pyplot as plt

# img = open("PC.png", 'rb')

# img = Image.open('PC0.png')  #打开图像

# img = Image.open("temp.png")  # 打开图像
# box = (10, 450, 100, 600)
# roi = img.crop(box)
#
# roi.save("cutPicture0.png")

img = Image.open("temp.png")  # 打开图像
box = (10, 450, 100, 600)
roi = img.crop(box)
roi.save("cutPicture2.png")

# plt.subplot(1,2,2),plt.title('roi')
# plt.imshow(roi),plt.axis('off')
# plt.show()