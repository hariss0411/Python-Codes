import math;
import itertools;
def check_prime(n):
  if n==2:
    return True
  elif n>2 and n%2==0:
    return False
  else:
    max_divison=math.floor(math.sqrt(n))
    for i in range(3,1+max_divison,2):
      if n%i==0:
        return False
  return True
  
n1,n2=map(int,input().split())
p1=[]
for i in range(n1,n2):
  if check_prime(i):
    p1+=[i]
comb=list(itertools.combinations(p1,2))
li=[]
for i in comb:
  temp=list(itertools.permutations((i)))
  li+=[int("".join(map(str,temp[0])))]+[int("".join(map(str,temp[1])))]
p2=[]
for i in li:
  if check_prime(i):
    p2+=[i]
p2=list(set(p2))
co=len(p2)
fibo=[0]*co
fibo[0],fibo[1]=min(p2),max(p2)
for i in range(2,co):
  fibo[i]=fibo[i-1]+fibo[i-2]
print(fibo[-1],end="")
