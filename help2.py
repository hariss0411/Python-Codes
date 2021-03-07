# # n=input()
# # k=int(input())
# # co=0
# # for i in range(int(n)+1):
# #     if sum(list(map(int,list(str(i)))))%k==0:
# #         co+=1
# # print(co%(10**9+7))
# n=int(input())
# k=int(input())
# co=0
# while co<k:
#     n+=1
#     if sum(list(map(int, list(str(n))))) % 5 == 0:
#         co+=1
#         print(n)
# print(n)
co=0
for i in range(1000):
    if i%7==4 and i%11==9:
        co+=1
print(co,(43**101+23**101)%66)