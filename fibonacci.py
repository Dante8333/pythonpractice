def fibonacci(n):
    a=0
    b=1
    if n<0:
        print('invalid input')
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
    return c
print(fibonacci(int(input('enter value for fibonacci '))))
    
        