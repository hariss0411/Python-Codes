t1,t2,t3=[],[],[]
f=0
for i in range(9):
    inp=int(input())
    if i%3==0:
        t1+=[inp]
    elif i%3==1:
        t2+=[inp]
    else:
        t3+=[inp]
    if inp<1 or inp >100:
        f=1
if f==0:
    avg=[]
    avg+=[round(sum(t1)/3)]
    avg+=[round(sum(t2)/3)]
    avg+=[round(sum(t3)/3)]
    ma=max(avg)
    c=0
    for i in range(3):
        if avg[i]>70 and avg[i]==ma:
            print(avg,"Trainee number:",i+1)
            c+=1
        if c==0 and i==2:
            print("All trainees are unfit")
else:
    print("INVALID INPUT")
