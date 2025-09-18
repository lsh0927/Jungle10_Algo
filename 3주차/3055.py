# from collections import deque

# R, C = map(int, input().split())
# grid = []
# for _ in range(R):
#     grid.append(list(input().strip()))

# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# q = deque()
# visit = [[False] * C for _ in range(R)]

# # 물의 위치들을 먼저 큐에 넣기
# for i in range(R):
#     for j in range(C):
#         if grid[i][j] == '*':
#             q.append(('*', i, j, 0))

# # 고슴도치 위치 넣기
# for i in range(R):
#     for j in range(C):
#         if grid[i][j] == 'S':
#             q.append(('S', i, j, 0))
#             visit[i][j] = True

# while q:
#     type, cy, cx, time = q.popleft()
    
#     if type == '*':  # 물 처리
#         for i in range(4):
#             ny, nx = cy + dy[i], cx + dx[i]
#             if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '.':
#                 grid[ny][nx] = '*'
#                 q.append(('*', ny, nx, time + 1))
    
#     else:  # 고슴도치 처리
#         if grid[cy][cx] == 'D':  # 도착
#             print(time)
#             exit()
        
#         for i in range(4):
#             ny, nx = cy + dy[i], cx + dx[i]
#             if 0 <= ny < R and 0 <= nx < C and not visit[ny][nx]:
#                 if grid[ny][nx] == '.' or grid[ny][nx] == 'D':
#                     visit[ny][nx] = True
#                     q.append(('S', ny, nx, time + 1))

# print("KAKTUS")

from collections import deque

R,C= map(int,input().split())
grid=[]

for _ in range(R):
    grid.append(list(input().strip()))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

water_q= deque()
hedgehog_q= deque()

#물과 고슴도치 위치 찾기

for i in range(R):
    for j in range(C):
        if grid[i][j]=="*":
            water_q.append((i,j))
        elif grid[i][j]=="S":
            hedgehog_q.append((i,j))

visit= [[False] * C for _ in range(R)]

# 고습도치 시작점 방문처리
for i in range(R):
    for j in range(C):
        if grid[i][j]=="S":
            visit[i][j]=True
            break

time=0

# 조건은 고슴도치가 움직일 수 있을 때
while hedgehog_q:
    time+=1

    #1단계: 물 먼저 퍼뜨리기
    water_size= len(water_q)
    for _ in range(water_size):
        cx,cy= water_q.popleft()

        for i in range(4):
            nx,ny=cx+dx[i], cy+dy[i]
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
                grid[nx][ny]="*"
                water_q.append((nx,ny))

    hedgehog_size= len(hedgehog_q)
    for _ in range(hedgehog_size):
        cx,cy= hedgehog_q.popleft()

        for i in range(4):
            nx, ny= cx+dx[i], cy+dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny]:
                if grid[nx][ny]=="D":
                    print(time)
                    exit()
                elif grid[nx][ny]==".":
                    visit[nx][ny]=True
                    hedgehog_q.append((nx,ny))
    

print("KAKTUS")