def isprime(n):
    if n==1 or n==0:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
N=int(input())
count=0
for i in range(N+1):
    for j in range(i,N+1):
        su=0
        if len(str(i)) >1:
            su+=sum(list(map(int,str(i))))
        else:
            su+=i
        if len(str(j)) >1:
            su+=sum(list(map(int,str(j))))
        else:
            su+=j
        if isprime(su):
            count+=1
print(count)
        
        
