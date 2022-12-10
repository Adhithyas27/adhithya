a=[44,66,55,77,3,2,8,6,88,9,3,7,90,555555,0,1,2]
oddnos=[]
evennos=[]
for i in range (len(a)):
       if(a[i]%2==0):
         evennos.append(a[i])
       else:
          oddnos.append(a[i])

print("odd nos=",(sorted(oddnos)))
print("even nos=",(sorted(evennos)))
