#Atousa-Niazi-Abkoh-98440127-OSLab--t3-8 -Math-Smallest common multiple-Python

print('enter n1 and n2:')
n1 = int(input())
n2 = int(input())
max_n=max(n1,n2)
max_end=n1*n2 # max_end=n1*n2 - max_n  i think its right 
for i in range(1,max_end+1):  # it repeat from 1 to max_end
    if(max_n % n1 == 0 and max_n % n2 == 0):
        print('the smallest common multiple is :',max_n)
        break;
    else:
        max_n+=1