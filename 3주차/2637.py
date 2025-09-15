import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq

n=int(input())
m=int(input())

graph= [[] for _ in range(n+1)]
degree= [0] * (n+1)
needs= [ [0] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    x,y,z= map(int,input().split())
    graph[y].append((x,z))
    degree[x]+=1


q= deque()

for i in range(1,n+1):
    # degree가 0이 아니라면 
    if degree[i] >0:
        q.append(i)    

while q:
    cur= q.popleft()

    for next, next_need in graph[cur]:
        if needs[cur].count(0)==n+1:
            needs[next][cur]+= next_need
        else:
            for i in range(1,n+1):
                needs[next][i]+=needs[cur][i] * next_need
        degree[next] -= 1
        if degree[next]==0:
            q.append(next)

for x in enumerate(needs[n]):
    if x[1]>0:
        print(*x)

        