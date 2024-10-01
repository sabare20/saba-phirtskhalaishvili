n_th_number=int(input('enter number from 0 to 20 :'))
num_0=0
num_1=1
num_place=0
while num_place<=n_th_number:
    if num_place==0 or num_place==1:
        print(num_place,end=' ')
    elif num_place>1 and num_place<20:
        num_n=num_0+num_1
        print(num_n,end=' ')
        num_0=num_1
        num_1=num_n
    num_place+=1
print()
print(f'{n_th_number}-th number is {num_n}')

   
    