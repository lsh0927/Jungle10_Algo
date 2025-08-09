import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq


N,M= map(int,input().split())
seq= [ [] for _ in range(N+1)]
indegree=[0] * (N+1)

for _ in range(M):
    a,b= map(int,input().split())
    seq[a].append(b)
    indegree[b]+=1


result=[]


def topology_sort():
    q=deque()

    for i in range(1,N+1):
        #진입차수가 0인 정점이면 큐에 추가
        if indegree[i]==0:
            q.append(i)

    while q:
        cur= q.popleft()
        result.append(cur)

        for i in seq[cur]:
            # cur로부터 나가는 간선 제거
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)


topology_sort()

for i in result:
    print(i, end=' ')
