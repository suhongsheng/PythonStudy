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
    
    display = None;
    
    firstNumber = None;
    
    operate = None;

    def cal(self, firstNumber, operate, secondNumber):
        operator = {'+':self.service.add, "-":self.service.sub, "*":self.service.mul, '/':self.service.dev};
        return operator.get(operate)(firstNumber, secondNumber)
    

    def numberCallBack(self, number):
        self.display.set(self.display.get() + number);
        
    def operatorCallBack(self, newOperate):
        if(self.operate != None and self.firstNumber != None):
            # 计算前一次的操作
            self.firstNumber = self.cal(self.firstNumber, self.operate, float(self.display.get()));
        else:
            # 记录操作符，并存储第一个
            self.firstNumber = float(self.display.get());
        self.display.set("");
        self.operate = newOperate;
        
    def ACCallBack(self):
        self.firstNumber = None;
        self.operate = None;
        self.display.set("");
        
    def CallBack(self):
        pass;    
    
    def CalCallBack(self):
        if(self.operate == None and self.firstNumber == None):
            # TODO
            return;
        secondNumber = float(self.display.get());
        result = self.cal(self.firstNumber, self.operate, secondNumber);
        self.display.set(str(result));
        self.firstNumber = None;
        self.operate = None;
    
    def __init__(self, service):  
          
        Tkinter.Frame.__init__(self)  
        #
        self.service = service;
        
        self.pack(expand=Tkinter.YES, fill=Tkinter.BOTH)  
        self.master.title('Simple Calculater')  
        root = self;
        
        self.display = Tkinter.StringVar();
        buttonResult = Tkinter.Entry(root, textvariable=self.display, background='#909090');
        buttonResult.grid(row=0, column=0, columnspan=6, rowspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
    
        # 数字键
        i = 0;
        for key in('1234567890.'):
            button1 = Tkinter.Button(root, fg="red", bg='#E0E0E0', text=key, command=lambda keyTemp=key : self.numberCallBack(keyTemp));
            if(key == '0'):
                button1.grid(row=2 + int(i / 3), column=i % 3, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
                i = i + 2;
            else:
                button1.grid(row=2 + int(i / 3), column=i % 3);
                i = i + 1;
        # 符号
        i = 0;
        for key in('+-*/'):
            button1 = Tkinter.Button(root, text=key, command=lambda keyTemp=key : self.operatorCallBack(keyTemp), fg="#FF9341");
            button1.grid(row=2 + i, column=4, columnspan=2, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
            i = i + 1;
            
        Tkinter.Button(root, text="AC", command=self.ACCallBack).grid(row=7, column=0, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
        Tkinter.Button(root, text="-", command=self.CallBack).grid(row=7, column=1, columnspan=1, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);
        Tkinter.Button(root, text="=", command=self.CalCallBack).grid(row=7, column=2, columnspan=4, sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S, padx=0, pady=0);

