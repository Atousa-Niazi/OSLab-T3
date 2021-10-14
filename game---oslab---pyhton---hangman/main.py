#Atousa Niazi-98440127-OSLab-python-Game- Hangman
# shart barande shodan
'''
Game : hangman (guess a word)
'''
import random

words_bank=['cat','dog','snake','chicken','hours','owl','eagle','sheep','mouse','lion','tiger','leperd','honeybadger','bees','pig','monkey','donkey','bear','fox','fish','trutle','duck','panda','hen','camel','lama','deer','giraffe','cow']

#first way:
#random.choice(words_bank)

# second way : by index - from 0 to len(words_bank)-1
index=random.randint(0,len(words_bank)-1)
word=words_bank[index]
life=len(word)

#right guess
user_true_char=[]
''' print - for evry '''
while True:
    count_=0
    for char in word:
        if char in user_true_char:
            print(char,end='')
        else:
            count_+=1
            print('-',end='')
    if count_==0:
        print('\n you win')
        break
        
    user_char=input('\n please enter a character :')  #s
    
    if user_char in word:
        user_true_char.append(user_char)
        print('✔')
    else :
        life-=1
        print('❌')
        
   
    if life ==0 :
        print('Game over')
        break
    
   

