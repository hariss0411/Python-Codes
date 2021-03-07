'''li=input()
st=''
if len(li)%2==0:
    for i in range(0,len(li),2):
        st+=li[i+1]+li[i]
else:
    for i in range(0,len(li)-1,2):
        st+=li[i+1]+li[i]
    st+=li[-1]
    
print(st)
'''
'''
st=input().split()
print(len(st[-1]))
'''
n=int(input())
li=list(map(int,input().split()))
if n%2==0:
    while li:
        print(max(li),min(li))
        li.remove(max(li))
        li.remove(min(li))
        
else:
    while li:
        print(max(li),min(li))
        li.remove(max(li))
        li.remove(min(li))
        if len(li)==1:
            li+=[0]
