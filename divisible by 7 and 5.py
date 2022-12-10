l=[3,99,3,5,10,15,20,25,30,35,7,14,21,70]
divisible_by_5=[]
divisible_by_7=[]
divisible_by_both_7and5=[]

for i in range (len(l)):
       if(l[i]%5==0):
          divisible_by_5.append(l[i])

       if(l[i]%7==0):
          divisible_by_7.append(l[i])

       if(l[i]%5==0)  and  (l[i]%7==0):
           divisible_by_both_7and5.append(l[i])

print("the no divisible by 5 =",sorted(divisible_by_5))
print("the no divisible by 7 =",sorted(divisible_by_7))
print("the no divisible by 5 and 7 =",sorted(divisible_by_both_7and5))
