a=int(input("enter your salary"))
print("your salary is",a,"rs")

if(a<=150000):
    print("you no need to pay tax")

elif(a>150000 and a<=300000):
    p=10/100*a
    print("your tax amount is",p,"rs")

elif(a>300000 and a<=500000):
      q=20/100*a
      print("your tax amount is",q,"rs")

elif(a>500001 ):
     r=30/100*a
     print("your tax amount is",r,"rs")

