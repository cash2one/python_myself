# -*- coding:utf-8 -*-

import csv  # 标准库

# 由于csv库有自己的换行符，需要把open方法的newline设置为空，否则在Excel中会出现数据隔行。

filename = ""
row = ""

# 写入
with open(filename, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row)

# 读取
with open(filename, 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for _ in reader:
        print(_)

# 不使用csv标准库，自己解析
with open('t.csv', 'r') as f:
    rows = [line.strip().split(',') for line in f.readlines()]