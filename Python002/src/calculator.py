#!/usr/bin/python
# -*- coding: utf-8 -*-
wfile = open('./logs.txt', "a");

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

operator = {1:add, 2:sub, 3:mul, 4:dev};

operatorStr = {1:'+', 2:"-", 3:"*", 4:'/'} ;

def done(sel):
    x = float(input("第一个操作数："));
    y = float(input("第二个操作数："));
    result = operator.get(sel)(x, y);
    wfile.write("{x} {operator} {y} = {result}\n".format(x=x, y=y, operator=operatorStr.get(sel), result=result))
    wfile.flush();
    print("计算的结果是：{result}".format(result=result));

def logs():
    rfile = open("./logs.txt", "r")
    for line in rfile.xreadlines():
        print(line);
    rfile.close();

def entry():
    print('''-------请根据以下提示进行计算的选择-----------
    1.输入1选择加法！
    2.输入2选择减法！
    3.输入3选择乘法！''')
    print('4.输入"4"选择除法！')
    print('5.输入"4"选择除法！')
    print("'6'.退出")
    print("----------------------------------------")
    while True:
        sel = int(input("输入你的选择："))
        if(sel < 5):
            done(sel);
        elif sel == 5:
            logs();
        else:
            wfile.close();
            # 退出程序
            exit(0)
# 入口
entry();
