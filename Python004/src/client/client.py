#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *  
  
host = '127.0.0.1';
port = 9999;
bufsize = 1024l;
addr = (host, port);
client = socket(AF_INET, SOCK_STREAM);
client.connect(addr);

operatorStr = {1:'+', 2:"-", 3:"*", 4:'/'} ;

def done(sel):
    x = float(input("第一个操作数："));
    y = float(input("第二个操作数："));
    # 连接到服务器端，进行计算
    client.send("{x} {sel} {y}".format(x=x, sel=sel, y=y));
    data = client.recv(bufsize);
    print("{x} {sel} {y} = {result}".format(x=x, sel=operatorStr.get(sel), y=y, result=data));

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
            client.close() 
            exit(0)
# 入口
entry();
