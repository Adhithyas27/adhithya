a=int(input("enter the number:"))
n1,n2 =0,1
#n2=1
i=0
if(a<=0):
      print("fibbonaci doesnt occur in zero")
elif(a==1):
    print("0")
else:
    while i<a:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        i=i+1
