v=0
u=str(input("enter the word"))
for i in u:
      if(i.isalpha()):
        v+=1
print("the number of digit:",len(u)-v)
print("the number of alphabet:",len(u))

