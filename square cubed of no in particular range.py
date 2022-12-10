a=int(input("enter the lower limit:"))
b=int(input("enter the upper limit:"))
numbers=[]
squared_numbers=[]
cubed_numbers=[]

for i in range(a,b):
      numbers.append(i)
      squared_numbers.append(i*i)
      cubed_numbers.append(i*i*i)

print("numbers :",numbers)
print("squared numbers :",squared_numbers)
print("numbers :",cubed_numbers)
