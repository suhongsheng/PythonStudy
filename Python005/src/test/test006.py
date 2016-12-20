#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter;  # 导入 Tkinter 库
import tkMessageBox;

root = Tkinter.Tk();  # 创建窗口对象的背景色

buttonResult = Tkinter.Entry(root, text="", background='#909090');
buttonResult.grid(row=0, column=0, columnspan=6, rowspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

def numberCallBack():
    buttonResult.setvar("text", "dd")
    
def operatorCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World");

def ACCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World");
    
def CallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World");
    
def CalCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World");   
    
# 数字键
i = 0;
for key in('1234567890.'):
    button1 = Tkinter.Button(root,fg="red", bg='#E0E0E0', text=key, command=numberCallBack);
    if(key == '0'):
        button1.grid(row=2 + int(i / 3), column=i % 3, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
        i = i + 2;
    else:
        button1.grid(row=2 + int(i / 3), column=i % 3);
        i = i + 1;
# 符号
i = 0;
for key in('+-*/'):
    button1 = Tkinter.Button(root, text=key, command=operatorCallBack, fg="#FF9341");
    button1.grid(row=2 + i, column=4, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
    i = i + 1;
    
Tkinter.Button(root, text="AC", command=ACCallBack).grid(row=7, column=0, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
Tkinter.Button(root, text="-", command=CallBack).grid(row=7, column=1, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
Tkinter.Button(root, text="=", command=CalCallBack).grid(row=7, column=2, columnspan=4, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

root.mainloop();  # 进入消息循环
