input_str=str(input('enter your string :'))
lenght_text=len(input_str)
i=-1
reverse_str=''
while -i<=lenght_text:
    if input_str[i].isalpha() or input_str[i] == '-':    # ასევე ეს შეზღუდვა შეიძლება ჩიწეროს ასე :if ord(input_str[i+1])<=65 or ord(input_str[i+1])>=122 and ord(input_str[i+1])!=ord('-'): 
        print(input_str[i],end='')
        reverse_str+=input_str[i].lower()
    i-=1  
    
print()
if input_str.lower()==reverse_str:
    print('is palindorme ')
else:
    print('is not palindorme')