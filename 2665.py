import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = []
for i in range(N):
    arr.append(input().strip())

def bfs():
    dist= [ [float('inf')] * N for _ in range(N)]
    dist[0][0]=0
    q=deque()
    q.append((0,0))

    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx,ny= cx+dx[i], cy+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                cost= 0 if arr[nx][ny]=='1' else 1

                if dist[nx][ny] > dist[cx][cy]+cost:
                    dist[nx][ny] = dist[cx][cy]+cost

                    if cost==0:
                        q.appendleft((nx,ny))
                    else:
                        q.append((nx,ny))

    return dist[N-1][N-1]

print(bfs())
