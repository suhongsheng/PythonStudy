#!/usr/bin/python
# -*- coding: utf-8 -*-

import CalculatorService;
import CalculatorView;

def main():
    print('start calculator.......');
    service = CalculatorService.CalculatorService();
    CalculatorView.CalculatorView(service).mainloop();

# 程序的入口  
if __name__ == '__main__':  
    main();
