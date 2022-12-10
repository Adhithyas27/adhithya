u=[77,9,6,77,8,9,99,10,6,3,4,2,22,55,33]
print("before sorting:",u)
i=sorted(u)
print("after sorting:",i)
a=int(input("enter the mth maximum number:"))
b=int(input("enter the nth minimum number:"))
print("the mth maximum number  is ",i[-a])
print("the nth minimum number  is ",i[b-1])
