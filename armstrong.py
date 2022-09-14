def armstrong(num):
    x= num
    sum1 = 0
    power = len(str(num))
    while num!=0:
        digit = num%10
        sum1 = sum1 + (digit**power)
        num = num // 10
    print(sum1)
    if x == sum1:
        print("given number is armstrong number:",x)
    else:
        print("given number is armstrong nummber:",x)
armstrong(num= int(input('enter value: '))) 