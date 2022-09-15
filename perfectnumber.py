def perfectnumber(num):
    sum1=1
    i = 2
    while i < num:
        if num  % i == 0:
            sum1 = sum1+i 
        i += 1
    if(sum1 == num):
        print('given number is perfect number: ',num )
    else:
        print('given number is not perfect number: ',num )
perfectnumber(int(input('enter value: ')))