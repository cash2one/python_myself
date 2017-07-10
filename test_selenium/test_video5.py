# -*- encoding:utf8 -*-
import re
import sys
import urllib2
import urllib
import os


reload(sys)
sys.setdefaultencoding("utf-8")

#a = 1
url_name = []
def get(pageindex):
    url = 'http://www.budejie.com/video/' + str(pageindex)
    # var1.set('已经获取到第%s页的视频视频'%(a))
    print url
    html = urllib.urlopen(url).read()
    url_reg = r'data-mp4="(.*?)"'
    url_items = re.findall(url_reg, html)
    name_reg = re.compile('<div class="j-r-list-c-desc".*?<a href=".*?>(.*?)</a>.*?</div>', re.S)
    name_items = re.findall(name_reg, html)
    for i, k in zip(name_items, url_items):
        url_name.append([i, k])

#传入文件名和video地址
# def saveVideo(filename,videoUrl):
#     print 'Saving : %s ...'%filename
#     urllib.urlretrieve("http://mvideo.spriteapp.cn/video/2017/0507/e06838a4-32c3-11e7-81de-1866daeb0df1_wpcco.mp4", 'D:\\video\\%s.mp4'%filename)

#传入文件名和video地址
def saveVideo(filename,videoUrl):
    print 'Saving : %s ...'%filename
    urllib.urlretrieve(videoUrl,'D:\\video\\%s.mp4'%filename)

####main exec ####
# for pageindex in range(1,2):
#     get(pageindex)
#
# for index, item in enumerate(url_name):
#     saveVideo(index, item[1])

# print 'Saving : %s ...' % filename
urllib.urlretrieve("http://swf.ws.126.net/openplayer/v01/-0-2_M6SGF6VB4_M6SGHJ9BO-vimg1_ws_126_net//image/snapshot_movie/2011/5/A/U/M73VNEFAU-1430711943278.swf",
                   'D:\\video\\126.mp4')