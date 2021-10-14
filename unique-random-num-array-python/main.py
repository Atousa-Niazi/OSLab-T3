#Atousa-Niazi-Abkoh-98440127-OSLab--t3-2 - unique random num array-Python

import random

A=[]
print('enter array length :')
n=int(input())
for j in range(n):
    x=random.randint(0,100)
    if x not in A:
        A.append(x)

print('A=',A)