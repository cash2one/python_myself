#-*-coding:utf-8-*-
from PIL import Image
save_file = "test.png"
img1 = Image.open(save_file)
w, h = img1.size
# region = (220*3,320*3,420*3,380*3)//两个一起
##将图片放大3倍
out = img1.resize((w*3, h*3), Image.ANTIALIAS)

out.show()

region1 = (220*3, 320*3, 320*3, 380*3)
region2 = (320*3, 320*3, 420*3, 380*3)
cropImg1 = out.crop(region1)

cropImg2 = out.crop(region2)

cropImg1.show()