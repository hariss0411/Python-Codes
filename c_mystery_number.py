for _ in range(int(input())):
    n = int(input())
    s = ""
    while(n):
        s = str(n & 1 ^ n >> 1 & 1) + s
        n >>= 1
    print(int(s,2))