# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image

file_name = "picture/crop.png"

###########二值化算法
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img
###########二值化算法

img1 = Image.open(file_name)
img2 = img1.convert('L')
img3 = binarizing(img2, 200)

# img3.save("temp.png")
code1 = pytesseract.image_to_string(img3)

print code1