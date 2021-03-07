from math import gcd,ceil
for _ in range(int(input())):
  n,t,m=map(int,input().split())
  a=gcd(m,t)
  m//=a
  t//=a
  a=(round(m/t*1000000007))
  print(a)
