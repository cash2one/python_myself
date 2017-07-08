# -*- coding: utf8 -*-
import csv

class handleCsvDeal():

    # def __init__(self):
    #     print 11

    def writeFilesx(self,filesx,data):
        csvfile = file(filesx, 'ab+')
        # , 'ab+' 追加方式    , 'wb' 写入
        writersx = csv.writer(csvfile)

        # writer.writerow(['姓名', '年龄', '电话'])
        # data = [
        #     ('小河', '25', '1234567'),
        #     ('小芳', '18', '789456')
        # ]
        writersx.writerows(data)
        csvfile.close()

    def readFilesx(self, filesx):
        csvfile = file(filesx, 'rb')
        readersx = csv.reader(csvfile)

        for line in readersx:
            print line
        csvfile.close()

def main():
    spider = handleCsvDeal()
    data = [('sx', '15', '1234567'),('111', '25', '1234567')]
    sx  = "csv_test.csv"
    spider.readFilesx(sx)
    # spider.writeFilesx(sx,data)

if __name__ == '__main__':
    main()