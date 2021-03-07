for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    m1=max(arr)
    sum1=sum(arr[:n-k+1])
    for i in range(1,k):
        a=sum(arr[i:n-k+i+1])
        if a<sum1:
            sum1=a
    if sum1<m1:
        sum1=m1
    print(sum1)
