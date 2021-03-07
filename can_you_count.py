for _ in range(int(input())):
    s=input()
    vow=0
    vo=["a","e","i","o","u"]
    ans=1
    for i in s:
        if i in vo:
            vow+=1
            vo.remove(i)
            #print(vow,vo)
        elif i=='_':
            ans=ans*vow
            #print(ans)
            #print(s[i],vow,vo)
    print(ans%9223372036854775808)
