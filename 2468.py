import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

max_height = max(map(max, arr))
max_val = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start_i, start_j, t):
    q = deque()
    q.append((start_i, start_j)) 
    visited[start_i][start_j] = True
        
    #와 진짜....
    while q:
        cx, cy = q.popleft() 
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if (0 <= nx < N and 0 <= ny < N and 
                not visited[nx][ny] and arr[nx][ny] > t):
                visited[nx][ny] = True
                q.append((nx, ny)) 
    

for T in range(0, max_height):
    visited = [[False] * N for _ in range(N)]
    total_cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] > T:
                bfs(i, j, T)
                total_cnt+=1
    
    max_val = max(max_val, total_cnt)

print(max_val)