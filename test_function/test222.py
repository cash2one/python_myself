# -*- coding:utf-8 -*-

header = {"Set-Cookie": "dkdk", "Set-Cookie": "222", "Set-Cookie": "455", "shs": "ncn"}
headers = dict()
for header_one in header:
    if header_one == "Set-Cookie":
        if "cookie" in headers:
            headers["cookie"] =  headers["cookie"] + header.get("Set-Cookie")
        else:
            headers["cookie"] = header.get("Set-Cookie")

print headers