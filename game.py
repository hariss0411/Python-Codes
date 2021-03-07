def game(string):
    le=len(string)
    c,v=0,0
    for i in range(le):
        if string[i] in ["A","E","I","O","U"]:
            v+=le-i
        else:
            c+=le-i
    if c>v:
        print("Stuart",c)
    elif v>c:
        print("Kevin",v)
    else:
        print("Draw")

s = input()
game(s)