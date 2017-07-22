# -*- coding: utf-8 -*-

import pickle

mydict = {"dhhd": "很好的", "test2": 747}

with open("test.pkl", "wb") as f:
    pickle.dump(mydict, f)

with open("test.pkl", "rb") as f:
    content = pickle.load(f)
    print type(content)
    print content

test2 = pickle.dumps(mydict)
content = pickle.loads(test2)
print content
