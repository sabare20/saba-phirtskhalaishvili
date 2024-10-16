import random 
comp_num=random.randint(1,100)
print(comp_num)
for i in range(1,11):
    player_num=int(input('enter number from 1 to 100 :'))
    if player_num>0 and player_num<100:
        if comp_num==player_num:
            print(f'you are winner, and number of trial is : {i}')
            break
        elif player_num!=comp_num and i<10:
            print(f'sorry try another number,number of trial is :{i}')
        elif  i>=10:
            print('number of trial is already 10,computer is winner')
            break
    else:
        print('entered number is out of range, please enter number from 1 to 100 ')
        exit(1)

