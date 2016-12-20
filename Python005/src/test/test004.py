#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter;  # 导入 Tkinter 库


import tkMessageBox;

root = Tkinter.Tk();  # 创建窗口对象的背景色

def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World");
   
buttonResult = Tkinter.Button(root, text="", command=helloCallBack);
buttonResult.grid(row=0, column=1, columnspan=4, rowspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=5, pady=5);

buttonAC = Tkinter.Button(root, text="AC", command=helloCallBack);
buttonAC.grid(row=2, column=1, columnspan=1);

button = Tkinter.Button(root, text="+/-", command=helloCallBack);
button.grid(row=2, column=2, columnspan=1);

buttonPer = Tkinter.Button(root, text="%", command=helloCallBack);
buttonPer.grid(row=2, column=3, columnspan=1);

buttonDiv = Tkinter.Button(root, text="/", command=helloCallBack);
buttonDiv.grid(row=2, column=4);


button1 = Tkinter.Button(root, text="1", command=helloCallBack);
button1.grid(row=3, column=1);

button2 = Tkinter.Button(root, text="2", command=helloCallBack);
button2.grid(row=3, column=2);

button3 = Tkinter.Button(root, text="3", command=helloCallBack);
button3.grid(row=3, column=3);

buttonMul = Tkinter.Button(root, text="*", command=helloCallBack);
buttonMul.grid(row=3, column=4);

button4 = Tkinter.Button(root, text="4", command=helloCallBack);
button4.grid(row=4, column=1);

button5 = Tkinter.Button(root, text="5", command=helloCallBack);
button5.grid(row=4, column=2);

button6 = Tkinter.Button(root, text="6", command=helloCallBack);
button6.grid(row=4, column=3);

buttonAdd = Tkinter.Button(root, text="+", command=helloCallBack);
buttonAdd.grid(row=4, column=4);

button7 = Tkinter.Button(root, text="7", command=helloCallBack);
button7.grid(row=5, column=1);

button8 = Tkinter.Button(root, text="8", command=helloCallBack);
button8.grid(row=5, column=2);

button9 = Tkinter.Button(root, text="9", command=helloCallBack);
button9.grid(row=5, column=3);

buttonAdd = Tkinter.Button(root, text="-", command=helloCallBack);
buttonAdd.grid(row=5, column=4);

button0 = Tkinter.Button(root, text="0", command=helloCallBack);
button0.grid(row=6, column=1, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

button0 = Tkinter.Button(root, text=".", command=helloCallBack);
button0.grid(row=6, column=3, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

buttonAdd = Tkinter.Button(root, text="=", command=helloCallBack);
buttonAdd.grid(row=6, column=4);

root.mainloop();  # 进入消息循环
