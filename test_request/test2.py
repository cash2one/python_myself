# -*- coding: utf-8 -*-

import requests
import traceback
def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)

        # requests.patch()
        # requests.post()
        # requests.head()
        # requests.patch()
        
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print traceback.format_exc()
        return "获取异常"

if __name__ == '__main__':
    url = "//www.baidu.com/link"
    print getHtmlText(url)
