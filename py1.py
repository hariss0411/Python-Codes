st=input()
c=1
for i in range(1,len(st)):
    if st[i]==st[i-1]:
        c+=1
    else:
        print("(",c, ",", st[i-1], ")", sep="")
        c=1
print("(",c, ",", st[-1], ")", sep="")