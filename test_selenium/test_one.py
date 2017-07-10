# -*- coding: utf-8 -*-
import re
from selenium import webdriver
import time
import requests
from browsermobproxy import Server

# 设置网路监控代理
server = Server(u"D:/pyCharm\myself_python/browsermob-proxy-2.0-beta-6-bin/browsermob-proxy-2.0-beta-6/bin/browsermob-proxy.bat")
# server = Server("/Users/Hao/anaconda/bin/browsermob/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

# 设置浏览器
# profile = webdriver.FirefoxProfile()
# profile.set_proxy(proxy.selenium_proxy())
# driver = webdriver.Firefox(firefox_profile=profile)

driver = webdriver.PhantomJS(executable_path=u"E:\python\phantomjs-1.9.7-windows\phantomjs.exe")

##得到监控
proxy.new_har("bilibili")
# 得到网页源代码
redirect_url = "http://www.bilibili.com/video/av9974036/"
print redirect_url
driver.get(redirect_url)

# 打开视频
# driver.find_element_by_name("pause_button").click()

driver.find_element_by_id("bofqi").click()

time.sleep(1)
# 得到网络监控数据，json数据
content = proxy.har  # returns a HAR JSON blob
server.stop()
driver.quit()

# 视频链接分析
video_box = []
data = content['log']['entries']
for j in range(len(data)):
    url = data[j]['request']['url']
    if url.find("mp4") != -1:
        print(url)
        video_box.append(url)

# 视频下载，存储到data文件夹
if len(video_box) >= 2:
    hd_video_url = video_box[1]
    video = requests.get(hd_video_url, timeout=10)
    string = u"D:/video/data/2.mp4"
    fp = open(string, 'wb')
    fp.write(video.content)
else:
    print("视频下载出现问题，视频页面不存在")