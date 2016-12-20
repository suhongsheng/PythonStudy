#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import os

def add(val1, val2):
    return val1+val2;

def sub(val1, val2):
    return val1 - val2;

def mul(val1, val2):
    return val1*val2;

def div(val1, val2):
    val = 0;
    try:
        val = val1/val2;
    except ZeroDivisionError as e:
        val = None;
    return val;

    
def inputNumber(str):    
    while 1:
        val = input(str);
        if float(val):
            return float(val);
        elif val.isdigit():
            return int(val);


def operate():
    operation = {'+':add,'-':sub,'*':mul,'/':div};

    flag = True;
    while(flag):
        op = raw_input("请输入想要进行计算的操作： 【+、-、*、/】: ");
        if op in operation:
            flag = False;
    
    val1 = inputNumber("Input the first number: ");
    val2 = inputNumber("Input the second number: ");

    result = operation[op](val1, val2);
    if result == None:
        print ("输入数据错误！");
        return;
    
    print ("Final result: " , result);
    



if __name__=='__main__':
    while(1):
        operate();
        val = input("Continue? (Y/N) ");
        if(val != 'Y'):
            print("Bye~");
            break;

        
