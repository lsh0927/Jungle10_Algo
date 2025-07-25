import sys,math
input= sys.stdin.readline
from collections import deque
# sys.stdin.readline는 개행문자를 포함한채로 비교

N,M,V= map(int,input().split())

graph= [ [] for _ in range(N+1)] 

for _ in range(M):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


# 방문 가능한 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문
for i in range(1,N+1):
    graph[i].sort()


def dfs(node):

    visited[node]=True
    li.append(node)

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


def bfs(node):
    q= deque()
    visited[node] = True
    li.append(node)
    q.append(node)

    while q:
        cur_node= q.popleft()

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node]=True
                q.append(next_node)
                li.append(next_node)
    


li=[]
visited= [False] * (N+1)    
dfs(V)

print(*li, sep=' ')

li.clear()
visited= [False] * (N+1)  
bfs(V)

print(*li, sep=' ')
