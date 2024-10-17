entered_num=int(input('enter number from 1 to 1000 :'))
if entered_num>1 and entered_num<1000:
    while True:
        if entered_num % 2 !=0:
            print(int(entered_num*3+1),end=' ')
            print('->',end=' ')
            entered_num=entered_num*3+1
        if entered_num % 2==0:
            print(int(entered_num/2),end=' ')
            entered_num=entered_num/2
            if entered_num==1:
                break
            print('->',end=' ')
else:
    print('entered number is out of range,please enter number from 1 to 1000 ')
    exit(1)
    