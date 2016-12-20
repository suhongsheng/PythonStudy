# -*- coding: utf-8 -*-
import Tkinter;

# 创建横条型框架  
def frame(root, side):  
    w = Tkinter.Frame(root);
    w.pack(side=side, expand=Tkinter.YES, fill=Tkinter.BOTH);
    return w;
# 创建按钮  
def button(root, side, text, command=None):  
    w = Tkinter.Button(root, text=text, command=command);
    w.pack(side=side, expand=Tkinter.YES, fill=Tkinter.BOTH);
    return w;
# 继承了Frame类，初始化程序界面的布局 

class CalculatorView(Tkinter.Frame):
    # service
    service = None;
    # 存储第一个数
    first = 0;
    # 存储第二个数
    second = 0;
    
    def __init__(self, service):  
          
        Tkinter.Frame.__init__(self)  
        #
        self.service = service;
        
        self.pack(expand=Tkinter.YES, fill=Tkinter.BOTH)  
        self.master.title('Simple Calculater')  
          
        display = Tkinter.StringVar()  
        # 添加输入框  
        Tkinter.Entry(self, relief=Tkinter.SUNKEN,
              textvariable=display).pack(side=Tkinter.TOP, expand=Tkinter.YES,
                                           fill=Tkinter.BOTH)  
        # 添加横条型框架以及里面的按钮  
        for key in('123', '456', '789', '-0.'):
            keyF = frame(self, Tkinter.TOP);
            for char in key:
                button(keyF, Tkinter.LEFT, char, lambda w=display, c=char:w.set(w.get() + c));
        # 添加操作符按钮  
        opsF = frame(self, Tkinter.TOP)  
        for char in '+-*/=':  
            if char == '=':  
                btn = button(opsF, Tkinter.LEFT, char)  
                btn.bind('<ButtonRelease - 1>', lambda e, s=self, w=display:s.calc(w), '+');
  
            else:  
                btn = button(opsF, Tkinter.LEFT, char, lambda w=display, s='%s' % char:w.set(w.get() + s))  
        # 添加清除按钮  
        clearF = frame(self, Tkinter.BOTTOM)  
        button(clearF, Tkinter.LEFT, 'clear', lambda w=display:w.set(''))  
  
    # 调用eval函数计算表达式的值  
    def calc(self, display):  
        try:  
            display.set(eval(display.get()))  
        except:  
            display.set("ERROR")  
