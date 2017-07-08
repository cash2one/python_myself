#!/usr/bin/env python
import re


def getDomain(s):
    res = s
    domainS = [".com", ".cn", ".com.cn", ".gov", ".net", ".edu.cn", ".net.cn", ".org.cn", ".co.jp", ".gov.cn", ".co.uk",
               "ac.cn", ".edu", ".tv", ".info", ".ac", ".ag", ".am", ".at", ".be", ".biz", ".bz", ".cc", ".de", ".es",
               ".eu", ".fm", ".gs", ".hk", ".in", ".info", ".io", ".it", ".jp", ".la", ".md", ".ms", ".name", ".nl",
               ".nu", ".org", ".pl", ".ru", ".sc", ".se", ".sg", ".sh", ".tc", ".tk", ".tv", ".tw", ".us", ".co", ".uk",
               ".vc", ".vg", ".ws", ".il", ".li", ".nz"]
    for l in domainS:
        regex = re.compile(r'[0-9a-zA-Z_-]+' + l + '$')
    m = regex.findall(s)
    if len(m) > 0:
        print m[0]
        return m[0]
    else:
        pass
    return res

if "__main__":
    print getDomain("www.baidu.com")