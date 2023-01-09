a=int(input("enter the number of fresh loaves purchased"))
c1=185*a
b=int(input("enter the number of day old loaves purchased"))
c2=b*(185-(60/100*185))
print("regular price=185.00rs")
print("Amount for new loaves:",c1)
print("Amount for day old loaves:",c2)
print("total amount=",c1+c2)


