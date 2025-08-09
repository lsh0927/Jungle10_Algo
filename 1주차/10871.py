import sys, math
input = sys.stdin.readline

N, X = map(int, input().split())
a = list(map(int, input().split()))


for i in range(0,N): 
    if a[i] < X:
        print(f'{a[i]} ', end='')