import sys
import heapq

input = sys.stdin.readline

n = int(input())
maze = []
for _ in range(n):
    maze.append(input().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[float('inf')] * n for _ in range(n)]

pq = [(0, 0, 0)]
dist[0][0] = 0

while pq:
    cost, x, y = heapq.heappop(pq)
    
    # 이미 처리된 노드라면 스킵
    if cost > dist[x][y]:
        continue
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 범위 체크
        if 0 <= nx < n and 0 <= ny < n:
            # 새로운 비용 계산 (흰 방: 0, 검은 방: 1)
            new_cost = cost + (0 if maze[nx][ny] == '1' else 1)
            
            # 더 적은 비용으로 갈 수 있다면 갱신
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny))

print(dist[n-1][n-1])