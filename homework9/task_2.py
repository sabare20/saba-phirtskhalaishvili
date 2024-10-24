from random import uniform
import math
n=int(input('enter positive integer :'))

for i in range(1,n+1) :
    a=uniform(0,1)
    b=uniform(0,1)
    counter=i
    if math.sqrt(a**2+b**2)<=1:
        counter+=1
        print(4*counter/n)
        