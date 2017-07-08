# -*- coding: utf-8 -*-
import traceback
import requests
import os

path = "D:/picture/"
url = "https://d2.xia12345.com/down/201612/25001/161225778.mp4"
file_path = path + url.split("/")[-1]
print file_path

try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    if not os.path.exists(path):
        os.mkdir(path)
    with open(file_path, "wb") as f:
        f.write(r.content)

except:
    print traceback.format_exc()

