# -*- coding:utf-8 -*-
import PIL.Image as Image
# import Image

class Test(object):
    def __init__(self):
        pass

    def image_joint(self, image_list, opt):  # opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
        image_num = len(image_list)
        image_size = image_list[0].size
        height = image_size[1]
        width = image_size[0]

        if opt == 'vertical':
            new_img = Image.new('RGB', (width, image_num * height), 255)
        else:
            new_img = Image.new('RGB', (image_num * width, height), 255)
        x = y = 0
        count = 0
        for img in image_list:

            new_img.paste(img, (x, y))
            count += 1
            if opt == 'horizontal':
                x += width
            else:
                y += height
        return new_img


def Main():
    sx = Test()
    image_list = list()

    cap = Image.open("capture.png", "r")
    cap_red = Image.open("capture_red.png", "r")
    image_list.append(cap)
    image_list.append(cap_red)
    dataimg = sx.image_joint(image_list, "vertical")

    dataimg.save("sx2.png")

    pass


if __name__ == '__main__':
    Main()