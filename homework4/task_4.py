num_0=0
num_1=1
place_n=int(input('enter integer from 0 to 20 :'))   
if place_n>=0 and place_n<20:
    for i in range(place_n+1):
        if i==0 or i==1:
            print(i)
        elif i>1 :
            num_n=num_0+num_1
            num_0=num_1
            num_1=num_n
            print(num_n)
        
    print(f'{place_n}-th number is :{num_n}')
else:
    print('entered number is wrong,please enter number from 0 to 20 :')
    exit(1)


    