import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq

n=int(input())
m=int(input())

graph= [[] for _ in range(n+1)]
degree= [0] * (n+1)

# 큐가 필요함 -> deque에서 관리
q= deque()

# needs 리스트로 개수 구하기
needs= [ [0] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    to,fro,cnt= map(int, input().split())
    degree[to]+=1
    graph[fro].append((to,cnt))

# 위상 정렬로 관리
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)


while q:
    cur = q.popleft()

    for next, next_need in graph[cur]:
        # 기본 제품
        # needs[cur]의 0의 개수를 셈으로써 기본 제품임을 확인
        # if needs[cur].count(0)==n+1:
        #     needs[next][cur]+= next_need
        
        # else:
        #     for i in range(1,n+1):
        #         needs[next][i]+=needs[cur][i] * next_need

        if needs[cur].count(0)==n+1:
            needs[next][cur] += next_need
        else:
            for i in range(1,n+1):
                needs[next][i]+=needs[cur][i] * next_need
        
        degree[next]-=1
        if degree[next]==0:
            q.append(next)


for x in enumerate(needs[n]):
    if x[1]>0:
        print(*x)







