'''words=input().split()
i=0
while i<len(words[0]):
    if words[0][i] in "aeiouAEIOU":
        words[0].replace("o","%")
        print(words[0],words[0][i])
    i+=1
i=0
while i<len(words[1]):
    if words[0][i] not in "aeiouAEIOU":
        words[1].replace(words[0][i],"#")
    i+=1
words[2]=words[2].upper()
print(" ".join(words))
'''
from collections import Counter
for _ in range(int(input())):
    n=int(input)
    li=list(map(int,input().split()))
    tot=0
    di={}
    for i in li:
        if  i in di.keys():
            di[i]+=1
            if di[i]==2:
                di[i]=0
                tot+=2
        else:
            di[i]=0
    print(tot)
