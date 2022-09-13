def simpleinterest(p,r,t):
    print("amount borrowed:",p)
    print("rate of interest:",r)
    print("time period:",t)
    si = p*r*t/100
    tm= si + p
    print("simple interest:",si)
    print("total amount with iterest:",tm)
simpleinterest(p=int(input("enter p: ")),r=int(input("enter r: ")),t=int(input("enter t: ")))
