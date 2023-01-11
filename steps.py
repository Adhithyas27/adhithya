def climbstairs(num):
    a=1
    b=2
    n=num-1
    for i in range(n):
        c=a
        a=a+b
        b=c
    return a
print(climbstairs(4))
