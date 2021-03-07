'''# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    a=input()
    check=[]
    check.append(bool(re.search(r"^[4-6]",a)))
    check.append(bool(re.search(r"^\d{4}\-?\d{4}\-?\d{4}\-?\d{4}$",a)))
    check.append(not(re.search(r"(\d)\-?\1\-?\1\-?\1",a)))
    if all(f for f in check):
        print("Valid")
    else:
        print("Invalid")
'''
for _ in range(int(input())):
    s=input()
    vow=0
    c=0
    vo=["a","e","i","o","u"]
    ans=1
    for i in s:
        if i in vo:
            vow+=1
            vo.remove(i)
            #print(vow,vo)
        elif i=='_':
            c+=1
            ans*=(vow)
            #print(s[i],vow,vo)
    print(c)


