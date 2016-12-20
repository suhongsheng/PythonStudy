#!/usr/bin/python
# -*- coding: utf-8 -*-

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

operator = {1:add, 2:sub, 3:mul, 4:dev} 

def done(sel):
    x = float(input("第一个操作数："))
    y = float(input("第二个操作数："))
    result = operator.get(sel)(x, y)
    print("计算的结果是：{result}".format(result=result))

def entry():
    print('''-------请根据以下提示进行计算的选择-----------
    1.输入1选择加法！
    2.输入2选择减法！
    3.输入3选择乘法！''')
    print('4.输入"4"选择除法！')
    print("'5'.退出")
    print("----------------------------------------")
    while True:
        sel = int(input("输入你的选择："))
        if(sel < 5):
            done(sel) 
        else:
            # 退出程序
            exit(0)
# 入口
entry();
