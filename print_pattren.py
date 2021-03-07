a=int(input())
i,j,k=0,0,1
while i<a:
    while j<i+1:
        print(k,end=" ")
        if k+1==a:k+=2
        else:k+=1
        j+=1
    print("")
    j=0
    k=1
    i+=1

    
