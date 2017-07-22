# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
#创建label使用Label实例化一个对象
textLabel=Label(root,text='您所下载的影片含有未成年人内容\n请满十八周岁后在点击下载！！！',justify=LEFT,padx=10)
textLabel.pack(side=LEFT)
#创建图片样式的Label首先用PhotImage实例化一个图片对象
#参数file的值为图片的位置
photo=PhotoImage(file='test.gif')
imaLabel=Label(root,image=photo)
imaLabel.pack(side=RIGHT)
mainloop()