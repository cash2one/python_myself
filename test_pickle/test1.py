# -*- coding: utf-8 -*-

import pickle

'''
    数据持久化
'''

file_name = "my_list.pkl"
# "E:\\my_list.pkl"

my_list = [123, 456, "小甲鱼", ['another list']]
#以二进制的方式写入
pickle_file = open(file_name, 'wb')
#向文件里写入数据用dump
#第一个参数是要写入的数据，第二个是要写入的文件
pickle.dump(my_list, pickle_file)
#写完以后别忘记将文件关闭，否则还会存储在
#缓冲里面，断电之后还会消失
pickle_file.close()
#到这里就将序列的数据存储到了文件里面

#读取文件中的内容
#对文件进行操作首先得获得文件的对象
pickle_file = open(file_name, "rb")
#将pickle_file中的数据加载到列表中去
my_list2 = pickle.load(pickle_file)
print(my_list2)