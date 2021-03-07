'''m1,m2,r1=map(int,input().split())
m1_m2,m1_r1,m2_r1=map(int,input().split())
m1_m2_r1=int(input())
print(r1-m1_r1-m2_r1+m1_m2_r1,m1_m2-m1_m2_r1)'''
p1=int(input())
l1=int(input())
p2=int(input())
l2=int(input())
r=int(input())
w=int(input())
t=int(input())

rt=(p1*l1)//r
if rt>t:
    r_l1=t*r
    temp=r_l1//l1
    ans=r_l1-temp*l1
    if ans ==0:
        print("READ", temp, l1, sep=" ")
    else:
        print("READ", temp, ans, sep=" ")
else:
    t1=t-rt
    w_l2=t1*w
    temp=w_l2//l2
    ans=w_l2- temp*l2
    if ans ==0:
        print("WRITE", temp, l2, sep=" ")
    else:
        print("WRITE",temp,ans,sep=" ")
        #from itertools import groupby
        #temp = set()
        # for i in st:
        #     if i not in temp:
        #         print("(",st.count(i),",",i,")",sep="")
        #     temp|={i}
        # for i,j in groupby(st):
        #     print("(", len(list(j)), ",", i, ")", sep="")
        #     # res=(len(list(j)),*i)
        #     # print(res,i)