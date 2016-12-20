#!/usr/bin/python
# -*- coding: utf-8 -*-

def falsefunc():
    print("in falsefunc......");
    return 0;

def truefunc():
    print("in truefunc......");
    return 2;

if truefunc()  and falsefunc() :
    print ("true.......")
else:
    print ("false......")

