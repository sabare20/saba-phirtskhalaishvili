first_str=str(input('enter your string :'))
second_str=str(input('enter your string :'))
lenght_second=len(second_str)
feasible_str=True

for i in range(0,lenght_second):
    if second_str[i]  in first_str:
        first_str=first_str.replace(second_str[i],'',1)
    else:
        feasible_str=False
        break
if  feasible_str is not False:
    print('yes')
else:
    print('no')
