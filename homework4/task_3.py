my_number1=int(input('enter integer from 1 to 1000 :'))
for i in range(1,my_number1+1):
    if my_number1 % i==0:
        print(i,end=' ')

