# -*- coding: utf-8 -*-
# a = "2013-10-10 23:40:00"
#将其转换为时间数组
import time
import datetime

a = str(datetime.datetime.now()).split(".")[0]
print a

timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
print timeArray

#转换为时间戳:
timeStamp = int(time.mktime(timeArray))
# timeStamp == 1381419600
print timeStamp
print time.time()

timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print otherStyleTime

# string 转 时间戳
a = "2013-10-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))

# 时间戳 转string
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)  # 换为时间数组
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print otherStyleTime

# 获得三天前的时间的方法
import time
import datetime
#先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
print threeDayAgo
#转换为时间戳:
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
#转换为其他字符串格式:
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print otherStyleTime

import datetime
#获得当前时间
now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print otherStyleTime