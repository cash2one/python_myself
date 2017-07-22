# -*- coding: utf-8 -*-
import tkinter as tk

class APP:
     def __init__(self,master):
     #在主窗口中创建一个框架，通常控件的第一个参数都是在哪里创建
          frame=tk.Frame(master)
     #设置框架的位置
          frame.pack(side=tk.LEFT,padx=10,pady=10)
     #在Frame中添加一个按钮，并且设置按钮的上的文字，以及文字的前景色，背景色，以及为button添加响应函数
          self.hi_there=tk.Button(frame,text='打招呼',bg='black',fg='blue',command=self.say_hi)
          self.hi_there.pack()

     def say_hi(self):
           print('你好，我是GXY')

root=tk.Tk()
app=APP(root)
root.mainloop()