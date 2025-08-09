import sys,math
input= sys.stdin.readline

A,B,V = map(int, input().split())

# h=0
# date=0
# while(h<V):
#     date+=1
#     h+=A
#     if h>=V:
#         break
#     h-=B

# print(date)

V=V-A

if (V%(A-B)==0):
    x=V//(A-B)
else:
    x=V//(A-B)+1

print(x+1)