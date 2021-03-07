li=list(map(int,input().split()))
i,j=1,len(li)-2
a=[li[0]]
b=[li[j+1]]
while i<=j:
    if li[i]<=a[-1]:
        a+=[li[i]]
        i+=1
    if li[j]<=b[-1]:
        b+=[li[j]]
        j-=1
    else:
        break
print(a,b)
if i>j:
    print("yes")
else:
    print("No")
