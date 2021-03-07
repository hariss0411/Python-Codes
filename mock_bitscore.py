n=int(input())
li=list(map(int,input().split()))
i=0
od,ev=[],[]
while i<n:
  a=str(li[i])
  li[i]=int(str(int(max(a))*11+int(min(a))*7)[-2:])
  if i%2==0:
    ev+=[li[i]]
  else:
    od+=[li[i]]
  i+=1
li={}
p=0
for i in ev:
  if i//10 in li.keys():
    li[i//10]+=1
  else:
    li[i//10]=1
for i in li.keys():
  if li[i]>=3:
    p+=2
  elif li[i]==2:
    p+=1
print(li)
li={}
for i in od:
  if i//10 in li.keys():
    li[i//10]+=1
  else:
    li[i//10]=1
for i in li.keys():
  if li[i]>=3:
    p+=2
  elif li[i]==2:
    p+=1
print(li,p,end=" ")
