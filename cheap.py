for _ in range(int(input())):
    string = input()
    aCost = int(input())
    bCost = int(input())
    length = len(string)
    ans = 0
    for i in range(0,length//2):
        if(string[i] == '/' or string[length - i - 1] == '/'):
            if(i == length - i - 1):
                ans += min(aCost, bCost)
            elif(string[i] == string[length - i - 1]):
                ans += 2*min(aCost, bCost)
            elif(string[i] == 'b' or string[length - i - 1] == 'b'):
                ans += bCost
            else:
                ans += aCost
        elif(string[i] != string[length - i - 1]):
            ans = -1
            break
    print(ans)