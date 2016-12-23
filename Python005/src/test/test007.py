#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter;  # 导入 Tkinter 库

root = Tkinter.Tk();  # 创建窗口对象的背景色

display = Tkinter.StringVar()

global firstNumber;
firstNumber = None;

global operate;
operate = None;

# 加法
def add(a, b):
    return a + b;

# 减法 
def sub(a, b):
    return a - b;

# 乘法
def mul(a, b):
    return a * b;

# 除法
def dev(a, b):
    return a / b;

operator = {'+':add, "-":sub, "*":mul, '/':dev};

def cal(firstNumber, operate, secondNumber):
    return operator.get(operate)(firstNumber, secondNumber)

buttonResult = Tkinter.Entry(root, textvariable=display, background='#909090');
buttonResult.grid(row=0, column=0, columnspan=6, rowspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

def numberCallBack(number):
    display.set(display.get() + number);
    
def operatorCallBack(newOperate):
    global firstNumber;
    global operate;
    if(operate != None and firstNumber != None):
        # 计算前一次的操作
        firstNumber = cal(firstNumber, operate, float(display.get()));
    else:
        # 记录操作符，并存储第一个
        firstNumber = float(display.get());
    display.set("");
    operate = newOperate;
    
def ACCallBack():
    firstNumber = None;
    operate = None;
    display.set("");
    
def CallBack():
    pass;    

def CalCallBack():
    global firstNumber;
    global operate;
    if(operate == None and firstNumber == None):
        # TODO
        return;
    secondNumber = float(display.get());
    result = cal(firstNumber, operate, secondNumber);
    display.set(str(result));
    
# 数字键
i = 0;
for key in('1234567890.'):
    button1 = Tkinter.Button(root, fg="red", bg='#E0E0E0', text=key, command=lambda keyTemp=key : numberCallBack(keyTemp));
    if(key == '0'):
        button1.grid(row=2 + int(i / 3), column=i % 3, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
        i = i + 2;
    else:
        button1.grid(row=2 + int(i / 3), column=i % 3);
        i = i + 1;
# 符号
i = 0;
for key in('+-*/'):
    button1 = Tkinter.Button(root, text=key, command=lambda keyTemp=key : operatorCallBack(keyTemp), fg="#FF9341");
    button1.grid(row=2 + i, column=4, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
    i = i + 1;
    
Tkinter.Button(root, text="AC", command=ACCallBack).grid(row=7, column=0, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
Tkinter.Button(root, text="-", command=CallBack).grid(row=7, column=1, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
Tkinter.Button(root, text="=", command=CalCallBack).grid(row=7, column=2, columnspan=4, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

root.mainloop();  # 进入消息循环
