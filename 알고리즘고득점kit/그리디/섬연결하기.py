


# def solution(n, costs):
    
#     costs.sort(key=lambda x: x[2])
    
#     parents= list(range(n))
    
#     def find(a):    
#         if parents[a]==a:
#             return a
#         else:
#             parents[a]=find(parents[a])
#             return parents[a]

#     def union(a,b):
#         pa=find(a)
#         pb=find(b)
    
#         if pa!=pb:
#             parents[pb]=parents[pa]
    
#     answer=0
#     edge = 0
    
#     for a,b,cost in costs:
#         if find(a)!=find(b):
#             union(a,b)
#             answer+=cost
#             edge+=1
#             if edge==n-1:
#                 break
    
#     return answer

import heapq

def solution(n, costs):
    # 1. 그래프 구성 (인접 리스트)
    graph = [[] for _ in range(n)]
    for a, b, cost in costs:
        graph[a].append((cost, b))
        graph[b].append((cost, a))
    
    # 2. Prim 알고리즘
    visited = [False] * n
    heap = [(0, 0)]  # (비용, 정점) - 0번 정점에서 시작
    answer = 0
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if visited[node]:  # 이미 방문한 정점
            continue
        
        visited[node] = True
        answer += cost
        
        # 인접한 간선들을 힙에 추가
        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node))
    
    return answer
