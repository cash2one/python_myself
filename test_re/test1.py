# -*- coding: utf-8 -*-

import re

str1 = "xiaobai python"

ma = re.match(r'xiaobai', str1)

print ma.group()

pa = re.compile(r'xiaobai')
sx = pa.match(str1)
print sx.group()
