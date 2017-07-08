
# -*- coding: UTF-8 -*-

import time;  # 引入time模块
import csv


class test():

    def test(self):
        # ticks = time.time()
        # print "当前时间戳为:", ticks
        # print 11
        # # 格式化成2016-03-20 11:45:39形式
        # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #
        # # 格式化成Sat Mar 28 22:24:24 2016形式
        # print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
        #
        # # 将格式字符串转换为时间戳
        # a = "Sat Mar 28 22:24:24 2016"
        # print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

        # fo = open("foo.txt", "wb")
        # fo.write("www.runoob.com!\nVery good site!\n");
        # print 11
        # # 关闭打开的文件
        # fo.close()

        csvfile = file('csv_tes.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerow(['姓名', '年龄', '电话'])

        data = [
            ('小河', '25', '1234567'),
            ('小芳', '18', '789456')
        ]
        writer.writerows(data)
        csvfile.close()



def main():
    # spider = test()
    # spider.test()
    import cookielib;
    import urllib2;

    # https: // www.baidu.com /
    # http: // hi.baidu.com / motionhouse
    loginUrl = "https: // www.baidu.com /";
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    resp = urllib2.urlopen(loginUrl);
    print 11
    for index, cookie in enumerate(cj):
        print '[', index, ']', cookie;

if __name__ == '__main__':
    main()