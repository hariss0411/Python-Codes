s=[input()]
c=0
for i in range(len(s[0])):
    temp=s[0][:i]+"*"+s[0][i+1:]
    s+=[temp]
se=[]
for a in s:
    se+=[a[i: j] for i in range(len(a)) 
          for j in range(i + 1, len(a) + 1)]
print(len(set(se))+1)
