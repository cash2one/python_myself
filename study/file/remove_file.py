

# import shutil
# file = """D://aaa"""
# shutil.rmtree(file)

import os
import shutil

delList = []
delDir = "D://aaaa"
delList = os.listdir(delDir)

for f in delList:
    filePath = os.path.join(delDir, f)
    if os.path.isfile(filePath):
        try:
            os.remove(filePath)
        except Exception, e:
            print filePath+"was not"
            pass
        print filePath + " was removed!"
    elif os.path.isdir(filePath):
        shutil.rmtree(filePath, True)
    print "Directory: " + filePath + " was removed!"