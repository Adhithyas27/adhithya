
#input
salary=int(input("enter your salary"))
sex=str(input("enter the sex of the employee (male/female):"))

if(sex=="male") and salary>=10000:
    e=salary+5/100*salary
    print("your special salary is",e)

if(sex=="female") and salary>=10000:
    f=salary+10/100*salary
    print("your special salary is",f)

if(sex=="male") and salary<=10000:
    d=salary+7/100*salary
    print("your special salary is",d)

if(sex=="female") and salary<=10000:
    p=salary+12/100*salary
    print("your special salary is",p)

        
