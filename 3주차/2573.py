import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def count_groups():
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    return cnt

def melt():
    melt_info = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                sea_count = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                        sea_count += 1
                if sea_count > 0:
                    melt_info.append((i, j, sea_count))
    
    for i, j, amount in melt_info:
        matrix[i][j] = max(0, matrix[i][j] - amount)

time = 0
while True:
    groups = count_groups()
    if groups >= 2:
        print(time)
        break
    elif groups == 0:
        print(0)
        break
    
    melt()
    time += 1