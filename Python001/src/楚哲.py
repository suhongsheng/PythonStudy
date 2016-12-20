print("一个高级的计算器")
temp = input("输入回车运算")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("选择运算密码：1234")
print("1加")
print("2减")
print("3乘")
print("4除")
ggg = input("输入(1/2/3/4)任意一个数字:")
num1 = int(input("请输入第一个数: "))
num2 = int(input("请输入第二个数: "))
if ggg == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif ggg == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif ggg == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif ggg == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("非法输入")
