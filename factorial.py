def factorial(n):
    if (n<0):
        return 0
    elif(n==0 or n==1):
        return 1
    else:
        factor = 1
        while(n>1):
            factor = factor*n
            n=n-1
    print("factor of given value :",factor )
factorial(5)