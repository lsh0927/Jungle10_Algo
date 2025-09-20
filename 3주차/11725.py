import sys,math
input= sys.stdin.readline
from collections import deque
# sys.stdin.readline는 개행문자를 포함한채로 비교

N=int(input())
graph= [[] for _ in range(N+1)]
trace= [-1] * (N+1)
visited= [False] * (N+1)

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q=deque([start])

    while q:
        cur= q.popleft()
        visited[cur]=True

        for next in graph[cur]:
            if not visited[next]:
                trace[next]=cur
                q.append(next)

bfs(1)
for val in trace:
    if val != -1:
        print(val)
