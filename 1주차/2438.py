import sys,math
input= sys.stdin.readline

N= int(input())

for i in range(1, N+1):
    for j in range(N-i+1,N+1):
        print('*', end='')
    print()