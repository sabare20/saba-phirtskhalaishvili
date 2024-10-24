input_num=int(input('enter yout number :'))
denominator=2*input_num-1
x=0
for i in range(1,denominator+1):
    if i%2!=0:
        if (i-1)%4==0:
            x+=4*(1/i)
        elif(i-1)%4!=4:
            x-=4*(1/i)
print(x)

