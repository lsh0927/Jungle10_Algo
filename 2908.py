import sys,math
input= sys.stdin.readline

print(max(int(x[::-1]) for x in input().split()))
