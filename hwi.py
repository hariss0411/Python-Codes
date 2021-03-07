def weightedUniformStrings(s, queries):
    result=[]
    a=s[0]
    if ord(a) in queries:
        result.append("Yes")
    else:
        result.append("No"
    con=a
    s=0
    for i in range(1,len(s)):
                      if a!=s[i]:
                con+=s[i]
                if s in queries:
                      result.append("Yes")
                else:
                      result.append("No")
        s1=ord(s[i])
        if s1 in queries:
                result.append("Yes")
        else:
                result.append("No")
            con=s[i]
            s=s1
        
            