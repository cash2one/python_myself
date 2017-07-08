
def encoding(data):
    types = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'iso-8859-1']
    for t in types:
        try:
            return data.decode(t)
        except Exception, e:
            print e
            pass
    return None

import requests
# "https://www.baidu.com/"
# "http://www.baidu.com/link?url=J0fqqn5129Caanoe3lt0nWzZVxxHMkbjMa1KfouaWom"
# "http://www.baidu.com/link?url=ymbtVYku57FhiclVrg9Nox_JSfQkIe4t07jYqeG6FYmtz9ha0Z_FXoVuSAfZRVjd_2BUQqkGF7X1u6I6PB5d0K"
r = requests.get("http://www.baidu.com/link?url=J0fqqn5129Caanoe3lt0nWzZVxxHMkbjMa1KfouaWom")

r.encoding = r.apparent_encoding

print(r.status_code)
print(r.text)

print(r.encoding)
print(r.apparent_encoding)

print(r.cookies)
print(r.headers)
print(r.history)

