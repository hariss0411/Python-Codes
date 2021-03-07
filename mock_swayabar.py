n=int(input())
bride=input()
groom=input()
flag=0
while bride and groom and flag<n:
  if bride[0] != groom[0]:
    groom=groom.replace(groom[0],"",1)+groom[0]
    flag+=1
  else:
    bride=bride.replace(bride[0],"",1)
    groom=groom.replace(groom[0],"",1)
    flag=0
  print(bride,groom)
print(len(groom),end=' ')
