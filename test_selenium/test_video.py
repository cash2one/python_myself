# -*- coding: utf-8 -*-
import re
from selenium import webdriver

#############找到要下载的链接#############
# browser = webdriver.Firefox()
# 如果不想看到浏览器，可以用无痕浏览器phantomJS
browser = webdriver.PhantomJS(executable_path=u"E:\python\phantomjs-1.9.7-windows\phantomjs.exe")
# 这边我们取B站鬼畜区排名页面，得到网页源代码
rank_url = "http://www.bilibili.com/ranking#!/origin/119/0/30/"

# 用Selnium的好处还在于返回的页面是js执行之后的页面。
browser.get(rank_url)
content = browser.page_source
browser.quit()

# 找到排名前100的视频页面
pattern = re.compile('<div class="rank-item"><div class="num">(.*?)'
                     '</div>.*?href="(.*?)"><div class="preview">.*?div class="title">(.*?)</div>', re.S)
item = re.findall(pattern, content)
base_url = "http://www.bilibili.com"

for i in range(len(item)):
    print (base_url + item[i][1]).split("\"")[0]

print item
