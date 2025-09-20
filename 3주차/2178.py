import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
visited = [[False] * M for _ in range(N)]

for i in range(N):
    str_line = input().rstrip()
    arr.append(str_line)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 1))  
    visited[x][y] = True
    
    while q:
        cx, cy, dist = q.popleft()
        
        if cx == N-1 and cy == M-1:
            return dist
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if (0 <= nx < N and 0 <= ny < M and 
                not visited[nx][ny] and arr[nx][ny] == '1'):
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    
    return -1  

print(bfs(0, 0))