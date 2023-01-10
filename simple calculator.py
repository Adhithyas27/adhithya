#basic calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
w=input("enter the operation [+,-,*,/]:")
if w=="+":
    print(a,"+",b,"=",add(a,b))
elif w=="-":
    print(a,"-",b,"=",sub(a,b))
elif w=="X":
    print(a,"X",b,"=",multiply(a,b))
elif w=="/":
    print(a,"/",b,"=",divide(a,b))
else:print("syntax error")


    

