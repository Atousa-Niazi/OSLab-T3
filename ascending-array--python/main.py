#Atousa-Niazi-Abkoh-98440127-OSLab--t3-6 - Ascending Array -Python

print("Enter number of elements :")
Array_num = []
n = int(input())
for i in range(0, n):
    item = int(input())
    Array_num.insert(i,item)
sorted_Array=Array_num.copy()   
sorted_Array.sort()
print(sorted_Array)
if sorted_Array is Array_num:
    print('A =',Array_num,"~~~~> ✔ (YES) it's sorted as ascending Array!")
else :
    print('A=',Array_num,"~~~~> ❌(NO) it's not sorted as ascending  Array!")