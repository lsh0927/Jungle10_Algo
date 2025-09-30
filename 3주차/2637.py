import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq

n=int(input())
m=int(input())

graph= [[] * (n+1) for _ in range(n+1)] 
degree= [0] * (n+1)
for _ in range(m):
    a,b,c= map(int, input().split())
    degree[a]+=1
    graph[b].append((a,c))

needs= [[0] * (n+1) for _ in range(n+1)]

q=deque()

for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)

while q:
    cur= q.popleft()

    for next, next_needs in graph[cur]:
        if needs[cur].count(0)==n+1:
            # 필요한 부품의 개수가 0인게 n+1개라면 기본 제품
            needs[next][cur] += next_needs
        else:
            # 중간 제품이므로 next에 중간제품을 넣을 때는 그안에 들어간 모든 부품을 더해줘야 함
            for i in range(1,n+1):
                needs[next][i]+= needs[cur][i] * next_needs
        
        degree[next]-=1
        if degree[next]==0:
            q.append(next)

for x in enumerate(needs[n]):
    if x[1]>0:
        print(*x)




