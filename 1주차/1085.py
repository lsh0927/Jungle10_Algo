import sys,math
input= sys.stdin.readline

x,y,w,h= map(int,input().split())


if x>=w/2:
    mx= w-x
else:
    mx= x

if y>=h/2:
    my= h-y
else:
    my= y


print(min(mx,my))