def primenumber(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
        
    return True
n=int(input('enter value: '))
for i in range(2,n+1):
    if (primenumber(i)):
        print(i)

        
    