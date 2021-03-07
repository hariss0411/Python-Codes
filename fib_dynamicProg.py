n=int(input())
mem=[0]*n
def fib(n):
    if n<=1:
        mem[n]=n
        return n
    else:
        if mem[n-1]!=0 and mem[n-2]!=0:
            return mem[n-1]+mem[n-2]
        else:
            return fib(n-1)+fib(n-2)
print(fib(n))
