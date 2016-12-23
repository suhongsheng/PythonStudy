# -*- coding: UTF-8 -*-
def menu():  
     print "this is a calculator"  
     print "what can i do:"  
     print " "  
     print "1) Addition"  
     print "2) Sub"  
     print "3) Multiplication"  
     print "4) Div"  
     print "5) Quit"  
     return input ("please select a number: ")  
  
def add(a, b):  
    res = a+b;
    print a, "+", b, "=", res  
    return res;
def sub(a, b):  
     print a, "-", b, "=", a - b  
     return a-b;
def mul(a, b):  
     print a, "*", b, "=", a * b  
     return a * b;
def div(a, b):  
     print a, "/", b, "=", a / b  


f = open("remember.txt", "a")  
choice = 0  
loop = 1  
while loop == 1:  
     choice = menu()  
     A = input("first number")
     B = input("second number")
     if choice == 5:
         loop = 0;
         break;
     elif choice == 1:  
          add(A, B)  
          f.write(str(A) + str("+") + str(B) + str("=") + str(add(A, B)))
     elif choice == 2:  
          sub(A, B)  
          f.write(str(A) + str("-") + str(B) + str("=") + str(sub(A, B)))
     elif choice == 3:  
          mul(A, B)
          f.write(str(A) + str("*") + str(B) + str("=") + str(mul(A, B)))
     elif choice == 4:  
          div(A, B)  
          f.write(str(A) + str("/") + str(B) + str("=") + str(div(A, B)))
f.close()
