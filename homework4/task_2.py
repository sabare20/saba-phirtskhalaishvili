import random
my_number=int(input('enter integer from 1 to 30 :'))

max_number=0
if my_number>=1 and my_number<30:
    for i in range(1,my_number) :
        random_num=random.randint(1,1000)
        print(random_num)
    
        if random_num>max_number:
            max_number=random_num
        
    print(f'max number is : {max_number}')
else:
    print('entered number is wrong,please enter integer from 1 to 30 :')
    exit(1)
    