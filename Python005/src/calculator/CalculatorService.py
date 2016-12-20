# -*- coding: utf-8 -*-

import Logger;

class CalculatorService:
    '计算器service，实现计算的核心内容'
    
    logger = Logger.Logger();
    # 加法
    def add(self, a, b):
        result = a + b;
        self.logger.log("%f + %f = %f" % (a, b, result));
        return result;
    
    # 减法 
    def sub(self, a, b):
        return a - b;
    
    # 乘法
    def mul(self, a, b):
        return a * b;
    
    # 除法
    def dev(self, a, b):
        return a / b;