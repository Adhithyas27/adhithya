age=int(input("enter your age:"))
s=18-age
if(age>18):
    print("you can vote")
elif(age==18):
    print("you are eligible to vote,apply voter id")
else:
    print('you are not eligible to vote wait for ',s,"years")
