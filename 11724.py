import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

N, M = map(int, input().split())

#유니온 파인드 풀이

# parent = [i for i in range(N+1)]

# def find(a):
#     if parent[a] == a:
#         return a
#     parent[a] = find(parent[a])  
#     return parent[a]

# def union(a, b):
#     pa = find(a)
#     pb = find(b)
    
#     if pa != pb: 
#         if pa > pb:
#             parent[pb] = pa
#         else:
#             parent[pa] = pb

# for _ in range(M):
#     u, v = map(int, input().split())
#     union(u, v)

# # 연결 요소 개수 세기
# roots = set()
# for i in range(1, N+1):
#     roots.add(find(i)) 

# print(len(roots))

#DFS 풀이


# visited= [False] * (N+1)
# edges=[[] for _ in range(N+1)]


# def dfs(cur_node):
#     visited[cur_node] = True

#     for next_node in edges[cur_node]:
#         if not visited[next_node]:
#             visited[next_node]=True
#             dfs(next_node)

# for _ in range(M):
#     u, v = map(int, input().split())
#     edges[u].append(v)
#     edges[v].append(u)

# answer=0

# for i in range(1,N+1):
#     if not visited[i]:
#         dfs(i)
#         answer+=1

# print(answer)


#BFS 풀이

visited= [False] * (N+1)
graph= [[] for _ in range(N+1)]
q=deque()

def bfs(node):
    q.append(node)

    while q:
        cur_node= q.popleft()
        visited[cur_node]=True

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                q.append(next_node)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer=0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        answer+=1

print(answer)