'''from math import prod
a=int(input())
for i in range(10,10001):
    if prod(list(map(int,str(i))))==a:
        print(i)
        break
else:
    print("Not Possible")
'''
n=int(input())
a=[]
for i in range(n):
    a+=[int(input())]
if n<2:
    print("Invalid Input")
else:
    a.sort()
    if  n == a.count(a[0]):
        print("Equal")
    else:
        print(a[0],a[1],sep=" ")
    
