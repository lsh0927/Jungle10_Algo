import sys,math
input= sys.stdin.readline

max=0
idx=-1

for i in range(1,10):
    a= int(input())
    if max < a:
        max=a
        idx=i

print(max)
print(idx)


