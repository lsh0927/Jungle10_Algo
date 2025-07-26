import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

start_city, end_city = map(int, input().split())

# DP 메모이제이션용
dp = [-1] * (n + 1)  # 각 정점에서 도착지까지의 최장 거리

def dfs(node):
    # 도착지에 도달했으면 0 반환
    if node == end_city:
        return 0
    
    # 이미 계산된 값이 있으면 반환
    if dp[node] != -1:
        return dp[node]
    
    dp[node] = 0
    # 현재 노드에서 갈 수 있는 모든 다음 노드 확인
    for next_node, weight in graph[node]:
        dp[node] = max(dp[node], dfs(next_node) + weight)
    
    return dp[node]

# 시작점에서 도착점까지의 최장 거리
max_time = dfs(start_city)

# 임계 경로의 간선 개수 계산 (모든 임계 간선의 총합)
critical_edges = 0
visited_edges = set()  # 중복 간선 방지

def count_critical(node):
    global critical_edges
    
    for next_node, weight in graph[node]:
        # 임계 경로상의 간선인지 확인
        if dp[node] == dp[next_node] + weight:
            # 간선 중복 체크 (node, next_node, weight)
            edge = (node, next_node, weight)
            if edge not in visited_edges:
                visited_edges.add(edge)
                critical_edges += 1
            count_critical(next_node)

count_critical(start_city)

print(max_time)
print(critical_edges)