import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq


m, n, h = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

answer = 0

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if matrix[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                queue.append((nx,ny,nz))
                matrix[nx][ny][nz] = matrix[x][y][z] + 1
                visited[nx][ny][nz] = True



for a in range(h):
    for b in range(n):
        for c in range(m):
            if matrix[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a,b,c))
                visited[a][b][c] = True
bfs()


#한개라도 1
for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(b))

print(answer-1)
