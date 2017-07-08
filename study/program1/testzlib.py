# coding : utf-8

import zlib


f = open('1sx.html', 'r')
content = f.read()
# s = "dshdhsdshdshjdshhdbdbddsbdsbvdsbkdbskbsddfsfsdkdsdskjdsjkdsdskjfdnfdnkdfdfkjndkj"
print len(content)

a = zlib.compress(content)
# print a
print len(a)
