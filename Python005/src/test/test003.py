#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter;  # 导入 Tkinter 库


import tkMessageBox;

root = Tkinter.Tk();  # 创建窗口对象的背景色

def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World");
   
button = Tkinter.Button(root, text="Hello,Python!", command=helloCallBack);
button.pack();

root.mainloop();  # 进入消息循环
