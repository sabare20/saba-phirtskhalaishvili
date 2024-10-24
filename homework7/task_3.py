entered_word=str(input('enter your word :'))
print(len(entered_word))
if len(entered_word)%2==0:
    for i in range(0,5):
        print(entered_word[int(len(entered_word))-1],end='')
        print(entered_word[0],end='')
        print(entered_word[int((int(len(entered_word))-1)/2+0.5)],end='')
        print(entered_word[int((int(len(entered_word))-1)/2-0.5)],end='')
        print()
elif len(entered_word)%2!=0:
    for i in range(0,5):
        print(entered_word[int(len(entered_word))-1],end='')
        print(entered_word[0],end='')
        print(entered_word[int(int((len(entered_word)-1))/2-0.5)],end='')
        print()    
