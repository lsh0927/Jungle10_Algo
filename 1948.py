# 다익스트라
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# edges = [[] for _ in range(n+1)]
# edges_rev = [[] for _ in range(n+1)]
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     edges[s].append([e, t])
#     edges_rev[e].append([s, t])

# s, d = map(int, input().split())


# def dijkstra():
#     distance = [0 for _ in range(n+1)]
#     q = deque([[0, s]])
#     while q:
#         dist, cur = q.popleft()
#         if distance[cur] > dist:
#             continue
#         for v, w in edges[cur]:
#             if dist + w > distance[v]:
#                 distance[v] = dist + w
#                 q.append([distance[v], v])
#     return distance


# def bfs():
#     cnt = 0
#     visited = [0 for _ in range(n+1)]
#     q = deque([e])
#     visited[e] = 1
#     while q:
#         cur = q.popleft()
#         for pre_v, pre_c in edges_rev[cur]:
#             if distance[pre_v] + pre_c == distance[cur]:
#                 cnt += 1
#                 if not visited[pre_v]:
#                     q.append(pre_v)
#                     visited[pre_v] = 1
#     return cnt


# distance = dijkstra()
# print(distance[d])
# print(bfs())


# 위상정렬 + 역방향 BFS
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

inDegree = [0 for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
edges_rev = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int, input().split())
    edges[s].append([e, t])
    edges_rev[e].append([s, t])
    inDegree[e] += 1

s, d = map(int, input().split())

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

dist = [0 for _ in range(n+1)]

while q:
    cur = q.popleft()
    for v, w in edges[cur]:
        if dist[cur] + w > dist[v]:
            dist[v] = dist[cur] + w
        inDegree[v] -= 1
        if inDegree[v] == 0:
            q.append(v)

cnt = 0
visited = [0 for _ in range(n+1)]
q = deque([d])

while q:
    cur = q.popleft()
    for v, w in edges_rev[cur]:
        if dist[v] + w == dist[cur]:
            cnt += 1
            if not visited[v]:
                visited[v] = 1
                q.append(v)

print(dist[d])
print(cnt)