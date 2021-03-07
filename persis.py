r,c=map(int,input().split())
li=[]
for i in range(r):
    li+=[list(map(int,input().split()))]
print("g")
def one_cal(i,j):
    lis=[]
    if j-1>0 and li[i][j-1]:lis.append((i,j-1))
    if j+1<c and li[i][j+1]:lis.append((i,j+1))
    if i+1<r and li[i+1][j]:lis.append((i+1,j))
    return lis
le,tem=0,0
lis=[]
for i in range(r):
        for j in range(c):
            if li[i][j]:lis+=one_cal(i,j)
            tem+=len(lis)+1
            while lis:
                a=len(lis)
                lis += one_cal(lis[0][0],lis[0][1])
                tem += len(lis)-a
                lis.pop(0)
            if le<tem:le=tem
            #print(lis)
            tem=0
print(le)
