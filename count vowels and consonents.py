a=str(input("enter the word"))
vowels=0
consonents=0
for i in a:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
         vowels+=1
      else:consonents+=1

print("enter the number of vowels:",vowels)
print("enter the number of consonents:",consonents)
