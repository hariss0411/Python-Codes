n=int(input())
li=[]
se=set()
for i in range(n):
    li+=[input()]
print(len(set(li)))
for i in li:
    if i not in se:
        se.add(i)
        print(li.count(i),end=" ")
