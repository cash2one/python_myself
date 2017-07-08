# -*- coding: utf8 -*-

import urllib2

opener = urllib2.build_opener()
url = '''https://www.baidu.com/fm_kl=021394be2f/from=844b/s?word=%E6%8B%9B%E8%81%98&sa=tb&ts=6710037&t_kt=0&ie=utf-8&rsv_t=071eLRbIgIYBbKnrSZJjiPI5uM7nvPfe%252F5Y9eKrtfssTv0c6pEV1l%252BtewQ&ms=1&rsv_pq=15339095230968024506&rqlang=zh&oq=%E6%8B%9B%E8%81%98'''
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
request = urllib2.Request(url, data=None, headers=headers)

response = opener.open(request, timeout=10)
header = response.info()
body = response.read()
if ('Content-Encoding' in header and header['Content-Encoding']) or \
        ('content-encoding' in header and header['content-encoding']):
    import gzip
    import StringIO
    d = StringIO.StringIO(body)
    gz = gzip.GzipFile(fileobj=d)
    body = gz.read()
    gz.close()

types = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'iso-8859-1']
for t in types:
    try:
        body = body.decode(t)
    except Exception, e:
        pass

print len(body)