input_num=int(input('enter number from 1 to 10000 :'))
num_str=str(input_num)
len_of_num=int(len(num_str))
x=0
sum_digit=0

if input_num>1 and input_num<10000:
    print(f'entered number :{input_num}')
    print('reversed number :',end='')
    while len_of_num-x>0:
        print(num_str[len_of_num-x-1],end='')
        x+=1
        sum_digit+=int(num_str[len_of_num-x-1])
    print()
    print(f'sum of digits : {sum_digit}')
else:
    print('entered number is out of range, please enter number from 1 to 10000 ')
    exit(1)
    
    