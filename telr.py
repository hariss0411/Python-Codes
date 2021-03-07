
s=input()
k=int(input())

from collections import Counter
cnt=0
for i in range(len(s)):
    for j in range(i,len(s)+1,k):
        co=Counter(s[i:j])
        for x in set(s[i:j]):
            if co[x]!=k or (j-i)<k:
                break
        else:
            if i!=j:
                cnt+=1
print(cnt)
