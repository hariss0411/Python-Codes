r,c=map(int,input().split())
li=[]
for i in range(r):
    li+=[list(map(int,input().split()))]
key_sort=int(input())
func=lambda x:x[key_sort]
li.sort(key=func)
for i in li:
    print(*i,sep="\t")