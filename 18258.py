import sys,math
input= sys.stdin.readline
from collections import deque

N=int(input())
q=deque()

for _ in range(N):
    op= list(map(str,input().split()))
    if op[0]=='push':
        q.append(op[1])
    elif op[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)   
    elif op[0]=='back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif op[0]=='size':
        print(len(q))
    elif op[0]=='empty':
        if not q:
            print(1)
        else:
            print(0)
    else:
        if q:
            print(q.popleft())
        else:
            print(-1)