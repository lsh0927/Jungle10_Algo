import sys,math
input= sys.stdin.readline
from collections import deque


N,M,K,X= map(int, input().split())
graph= [[] for _ in range(N+1)]
visited= [False for _ in range(N+1)]  # 1차원 배열


for _ in range(M):
    a,b= map(int,input().split())
    graph[a].append(b)

res=[]
def bfs():
    q=deque()
    q.append((0,X))
    visited[X]=True

    while q:
        cur_cost,cur= q.popleft()

        if cur_cost==K:
            res.append(cur)
            continue


        if cur_cost < K:  # K보다 작을 때만 계속 탐색
            for next in graph[cur]:
                if not visited[next]:
                    visited[next]=True
                    q.append((cur_cost+1,next))


bfs()
if res:
    res.sort()
    for city in res:
        print(city)
else:
    print(-1)