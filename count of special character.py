#count special chatacter
u=str(input("enter the word"))
p=0
q=0    
for i in u:
      if(i.isalpha()):
         p+=1
      elif(i.isdigit()):
           q+=1
print("the number of special chatacter:",len(u)-p-q)
         
         
