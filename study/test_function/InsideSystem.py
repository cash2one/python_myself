# -*- coding: utf8 -*-

import urllib
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class InsideSystem(object):

    def __init__(self):
        pass

    def send_InsideSystem(self, rankLists):
        try:
            response = urllib.urlopen("http://192.168.0.72:5000/Platform/receiveDate",
                                      data=rankLists
                                      )
            sx = response.read()
            print sx
        except Exception as e:
            import traceback
            traceback.print_exc()
            pass

def Main():
   sx = InsideSystem()
   # sx.send_InsideSystem("""rankLists=[{"keywordid":"100","imgData":"aHR0cHM6Ly9zczAuYmRzdGF0aWMuY29tLzVhVjFianFoX1EyM29kQ2Yvc3RhdGljL3N1cGVybWFuL2ltZy9sb2dvL2JkX2xvZ28xXzMxYmRjNzY1LnBuZw==","rank":"1"}]""")

if __name__ == '__main__':
    Main()
