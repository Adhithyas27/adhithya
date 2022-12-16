print("quadratic equation:ax^2+bx+c")
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
t=b**2-4*a*c
d=t**0.5
if(t>0):
    print("roots are real")
    root1=(-b+d)/2*a
    root2=(-b-d)/2*a
    print("the first solution is ",round(root1,2))
    print("the first solution is ",round(root2,2))
else:print("it has imagionary roots") 
    
          

    
          
