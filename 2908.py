import sys,math
input= sys.stdin.readline

a,b = map(str, input().split())

print(max(int(a[::-1]),int(b[::-1])))
