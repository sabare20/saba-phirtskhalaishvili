n=int(input('enter number form 1 to 10 :'))
x=-n+1

while n-abs(x)>0:
    i=1
    while n-abs(x)-i>=0:
        print(i,end='')
        i+=1
    print()
    x+=1
    
