import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq

n=int(input())
m=int(input())

q= deque()
degree= [0] * (n+1)

seq= [[] for _ in range(n+1)]
needs= [ [0] * (n+1) for _ in range(n+1)]
# needs[i][j] = i번 제품을 만들 때 필요한 j번 기본부품의 개수


for _ in range(m):
    a,b,c= map(int, input().split())
    seq[b].append((a,c))
    degree[a]+=1

for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)


while q:
    cur = q.popleft()   
    
    for next, next_need in seq[cur]:

        # 기본제품
        if needs[cur].count(0) ==n+1:
            needs[next][cur] += next_need

        # 중간제품
        else:
            for i in range(1,n+1):
                needs[next][i]+=needs[cur][i] * next_need
        # 차수 -1
        degree[next] -= 1
        if degree[next]==0:
            #차수 0이면 큐에 넣음
            q.append(next)

for x in enumerate(needs[n]):
    if x[1]>0:
        print(*x)

