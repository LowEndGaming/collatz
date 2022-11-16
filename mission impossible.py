f=0
n=0
for x in range(295147905179352825856,1267650600228229401496703205376):
    n=x
    f=0
    while x!=1:
        f=f+1
        if x%2==1:
            x=3*x+1
        elif x%2==0:
            x=x/2
        else:
            print(x)
    if x==1: 
        print(n,'follows and',f,'times')
