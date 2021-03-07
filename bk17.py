'''n=int(input())
arr=list(map(int,input().split(',')))
t1,t2=[],[]
for i in arr:
    if i%2==0:
        t2+=[i]
    else:
        t1+=[i]
i,j=0,0
if t1[0]<t2[0]:
        print(t1[0])
        i=1
        i,j=j,i
else:
    print(t2[0])
        
for i in range(n) :
    if i%2==0:
        print(t1[i])
        i+=1
    '''
input1=input()


temp=""
for i in input1:
    n=ord(i)
    n=n+3
    if n+3>122:
        t=n-122
        n=96+t
    temp+=chr(n)
print(temp)
