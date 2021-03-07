n=int(input())
li=[]
se=set()
for _ in range(n):
    te,te1=input().split()
    li+=[te]
    se.add(te,te1)
    print(set(te),se)
