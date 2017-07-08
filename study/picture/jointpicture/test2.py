# import skimage.io as io
# from skimage import data_dir
# str='d:/pic/*.jpg:d:/pic/*.png'
# coll = io.ImageCollection(str)
# print(len(coll))

from skimage import data_dir, io, color


def convert_gray(f):
    rgb = io.imread(f)
    return color.rgb2gray(rgb)


str = data_dir + '/*.jpg'
coll = io.ImageCollection(str, load_func=convert_gray)
io.imshow(coll[1])