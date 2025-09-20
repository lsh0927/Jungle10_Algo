import sys,math
input= sys.stdin.readline

N=int(input())


def recur(n):
    if(n==1):
        return 1
    else:
        return n * recur(n-1)    

if(N<=1):
    print(1)

else: 
    print(recur(N))