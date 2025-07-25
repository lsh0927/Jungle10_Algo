import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, visited):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and arr[nx][ny] > 0:
                dfs(nx, ny, visited)

def melt():
    tmp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    #if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    if arr[ni][nj] == 0:
                        cnt += 1
                tmp[i][j] = max(0, arr[i][j] - cnt)
    
    return tmp

time = 0

while True:
    # 빙산 덩어리 개수 세기
    visited = [[False] * M for _ in range(N)]
    ice_groups = 0
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                dfs(i, j, visited)
                ice_groups += 1
    
    # 빙산이 없으면 0 출력
    if ice_groups == 0:
        print(0)
        break
    
    # 두 덩어리 이상이면 시간 출력
    if ice_groups >= 2:
        print(time)
        break
    
    # 빙산 녹이기
    arr = melt()
    time += 1