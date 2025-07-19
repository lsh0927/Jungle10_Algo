import sys,math
input= sys.stdin.readline
from collections import deque

N=int(input())
q=deque()

for i in range(1,N+1):
    q.appendleft(i)

while N>1:
    q.pop()
    if len(q)==1:
        break
    q.appendleft(q.pop())

print(q[0])
