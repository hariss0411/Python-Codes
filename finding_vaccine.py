n=int(input())

n1=int(input())

s1=input()

l1=[]

for _ in range(n):

    l=int(input())

    s2=input()

    l1.append(s1.count('G')*s2.count('C')+s2.count('G')*s1.count('C'))

print(l1.index(max(l1))+1)