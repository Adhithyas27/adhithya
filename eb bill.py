a=float(input("enter the EB meter reading of last month:"))
b=float(input("enter the EB meter reading of this month:"))
c=b-a
print("you have been used ",c,"units this month")

if(c<=100):
    print("ur bill is",c*3.46,"rs")

if(c>101 and c<=500):
    print("ur bill is",c*7.43,"rs")

if(c>=501):
    print("ur bill is",c*10.32,"rs")
