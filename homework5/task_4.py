
"""
x is height of three  others are just variables for code.
"""


x=int(input('enter number from 1 to 50 :'))

for i in range(1,x+2):
    l=i
    if i==1:
        m=1
        while x-m>0:
            print(' ',end='')
            m+=1
        print('*')
        print(end='')
    elif i>1 and i<x+1:
        while x-i>0:
            print(' ',end='')
            i+=1
        for n in range(1,l):
            print('/',end='')
        print('|',end='')
        for t in range(1,l):
            print('\\',end='')
        print()
    elif i==x+1:
        k=1
        while x-k>0:
            print(' ',end='')
            k+=1
        print('|')
        
    
    

    