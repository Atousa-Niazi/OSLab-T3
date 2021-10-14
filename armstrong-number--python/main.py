#Atousa-Niazi-Abkoh-98440127-OSLab--t3-5 - Armstrong number -Python

print('enter a number:')
n_user=input()
x=len(n_user)
sum_n=0
n_int=int(n_user)

for i in range(x) :
    n=int(n_user[i])
    sum_n=n**x+sum_n
    
if sum_n==n_int:
    print('✔ (YES)the number is an Armstrong number.')
else:
    print('❌ (NO)the number is not an Aarmstrong number.!')
