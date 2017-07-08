# -*- coding: utf-8 -*-
import traceback
import os

import urllib2

path = "D:/picture/"
url = "MP4"
file_path = path + url.split("/")[-1]
print file_path
if not os.path.exists(path):
    os.mkdir(path)

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request, timeout=30)
    r = response.read()
    print len(r)
    with open(file_path, "wb") as f:
        f.write(r)
except:
    print traceback.format_exc()




