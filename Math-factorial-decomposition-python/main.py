#Atousa-Niazi-Abkoh-98440127-OSLab--t3-4 - factorial Decomposition-Python

print('please enter a number:')
n=int(input())
n_user=n
c=0
i=1
while True:
    if n==1:
        print('✔(YES)the num is a factorial result',n_user,'=',str(c)+'!')
        break
    elif n==0:
        print('⚠(ERROR)it doesnt exits!!!')
        break
    else:
        if n%i==0:
            n=n/i
            c+=1
            i+=1
        else :
            c=0
            print('❌(NO)the num is not a factorial result !')
            break
