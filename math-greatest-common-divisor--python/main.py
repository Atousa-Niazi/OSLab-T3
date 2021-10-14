#Atousa-Niazi-Abkoh-98440127-OSLab--t3-7 - Math-greatest common divisor -Python


print('enter n1 , n2 :')
n1=int(input())
n2=int(input())
min_n=min(n1,n2)
i_old=0
for i in range(1,min_n+1): # range default is 0-n-1 so we will give it a start and stop point
    if n1%i==0 and n2%i==0:
       if i==max(i_old,i):
           i_old=i
       
print('the greatest common divisor is:',i_old)