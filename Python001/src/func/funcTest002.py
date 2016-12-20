#!/usr/bin/python
# -*- coding: utf-8 -*-

def add(a, b):
    return a + b;

def ifunc1():
    print("in ifunc1......");
    return 5;

def ifunc2():
    print("in ifunc2......");
    return 4;

print(add(ifunc1(), ifunc2()))
