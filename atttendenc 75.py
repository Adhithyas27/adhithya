a=int(input("enter the attended class:"))
b=int(input("enter the total no of class:"))
k=a/b*100
print("your attendence percentage is:",k)
m=str(input("you have any medical issue (yes/no):"))

if(k>=75) and m=="no":
    print("you are eligible to write the exam")

if(k>=75) and m=="yes":
    print("you are eligible to write the exam")


if(k<75) and m=="no":
    print("you are not eligible to write the exam")

if(k>75) and m=="yes":
    print("you are eligible to write the exam")

