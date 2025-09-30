import sys,math
input= sys.stdin.readline
from collections import deque
import heapq as hq


m, n, h = map(int, input().split())

matrix = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]


q=deque()

tmp=0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if matrix[k][i][j]==1:
                tmp+=1
                q.append((k,i,j,0))
                visited[k][i][j]=True

if tmp==0:
    print(-1)
    exit()

time=0
while q:
    cz,cx,cy,time= q.popleft()

    for i in range(6):
        nx=dx[i]+cx
        ny=dy[i]+cy
        nz=dz[i]+cz

        if 0<=nx<n and 0<=ny<m and 0<=nz<h and not visited[nz][nx][ny] and matrix[nz][nx][ny] == 0:
            matrix[nz][nx][ny]=1
            visited[nz][nx][ny]=True
            q.append((nz,nx,ny,time+1))

for k in range(h):
    for i in range(n):
        for j in range(m):
            if matrix[k][i][j]==0:
                print(-1)
                exit()

print(time)