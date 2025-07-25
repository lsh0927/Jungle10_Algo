import sys,math
input= sys.stdin.readline
from collections import deque
# sys.stdin.readline는 개행문자를 포함한채로 비교


N=int(input())
graph= [[] for _ in range(N+1)]


def bfs(node):
    q=deque([node])
    visited[node]=True

    while q:
        cur_node= q.popleft()
        visited[cur_node]=True

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                trace[next_node]=cur_node
                q.append(next_node)


for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited= [False] * (N+1)

#각 노드의 부모가 저장될 곳
trace= [0] * (N+1)
bfs(1)

for i in range(2,N+1):
    print(trace[i])