#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
import pickle

from PIL import Image
import pytesseract
# from pytesser import *

save_file = "test2.png"

# phantomJs = u"E:\python\phantomjs-1.9.7-windows\phantomjs.exe"
# driver = webdriver.PhantomJS(executable_path=phantomJs)
# driver.set_page_load_timeout(30)
#
# ####################################第二步:利用cookie登录#####################################
# driver.get("http://index.baidu.com")
# cookies = pickle.load(open("cookies.txt", "rb"))
#
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.get("http://index.baidu.com/?tpl=trend&type=0&area=0&time=13&word=%C4%CC%B7%DB")
#
#
# # ---------------------------------------------
# # 近30 天
# e1 = driver.find_element_by_class_name("gColor1")
# e1.click()
# # ---------------------------------------------
#
# time.sleep(3)
# driver.get_screenshot_as_file(save_file)
# print("截屏结束.................")
# driver.quit()

# ###########二值化算法
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

# 处理图片
img1=Image.open(save_file)
w, h = img1.size
# region = (220*3,320*3,420*3,380*3)//两个一起
##将图片放大3倍
out=img1.resize((w*3, h*3),Image.ANTIALIAS)
region1 = (220*3, 320*3, 320*3, 380*3)
region2 = (320*3, 320*3, 420*3, 380*3)
cropImg1 = out.crop(region1)

# cropImg1.save("crop.png")

cropImg2 = out.crop(region2)
# 转化到灰度图
img1 = cropImg1.convert('L')
img2 = cropImg2.convert('L')

# img1.save("temp.png")
# img2.save("temp2.png")

img1 = binarizing(img1, 200)
img2 = binarizing(img2, 200)

# code1 = image_to_string(img1)
# code2 = image_to_string(img2)

code1 = pytesseract.image_to_string(img1)
code2 = pytesseract.image_to_string(img2)

 # 由于都是数字
# 对于识别成字母的 采用该表进行修正
rep = {'O': '0',
       'I': '1',
       'L': '1',
       'Z': '2',
       'S': '8',
       '?': '7'
       }
for r in rep:
    code1 = code1.replace(r, rep[r])
    code2 = code2.replace(r, rep[r])

print code1
print code2
print "整体搜索指数:" + str(code1).replace(".","").replace(" ",'')
print "移动搜索指数:" + str(code2).replace(".","").replace(" ",'')
img1.show()
img2.show()