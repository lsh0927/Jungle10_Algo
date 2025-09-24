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

# import sys
# input= sys.stdin.readline
# from collections import deque


# R,C= map(int,input().split())
# li=[]
# for _ in range(R):
#     li.append(list(input().strip()))


# q=deque()

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]


# visit= [[False] * C  for _ in range(R)]
# # 물 먼저 큐에 넣기
# for i in range(R):
#     for j in range(C):
#         if(li[i][j]=='*'):
#             q.appendleft((i,j,0))
#         if(li[i][j]=="S"):
#             q.append((i,j,0))
#             visit[i][j] = True


# while q:
#     cx,cy,ctime= q.popleft()
    
#     if(li[cx][cy]=='D'):
#         print(ctime)
#         exit()

#     # 큐의 순서대로 퍼뜨리기
#     for i in range(4):
#         nx= cx+dx[i]
#         ny= cy+dy[i]

#         if(0<=nx<R and 0<=ny<C and not visit[nx][ny] and li[nx][ny]=='.'):
#             if li[cx][cy]=='*':
#                 visit[nx][ny]=True
#                 li[nx][ny]='*'
#             elif li[cx][cy]=='S':
#                 visit[nx][ny]=True
#                 li[nx][ny]='S'
#             q.append((nx,ny,ctime+1))

# print("KAKTUS")


# import sys
# input = sys.stdin.readline
# from collections import deque

# R, C = map(int, input().split())
# li = []
# for _ in range(R):
#     li.append(list(input().strip()))

# q = deque()
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# visit = [[False] * C for _ in range(R)]

# # 물 먼저 큐에 넣기 (appendleft로 앞쪽에)
# for i in range(R):
#     for j in range(C):
#         if li[i][j] == '*':
#             q.appendleft((i, j, 0, '*'))  # 타입 정보 추가

# # 고슴도치 나중에 큐에 넣기 (append로 뒤쪽에)
# for i in range(R):
#     for j in range(C):
#         if li[i][j] == 'S':
#             q.append((i, j, 0, 'S'))  # 타입 정보 추가
#             visit[i][j] = True

# while q:
#     cx, cy, ctime, cell_type = q.popleft()
    
#     # 고슴도치가 목적지에 도달했는지 체크
#     if cell_type == 'S' and li[cx][cy] == 'D':
#         print(ctime)
#         exit()

#     # 4방향으로 퍼뜨리기/이동하기
#     for i in range(4):
#         nx = cx + dx[i]
#         ny = cy + dy[i]

#         if 0 <= nx < R and 0 <= ny < C:
#             if cell_type == '*':  # 물 처리
#                 if li[nx][ny] == '.':  # 물은 빈 공간으로만 퍼짐
#                     li[nx][ny] = '*'
#                     q.append((nx, ny, ctime + 1, '*'))
                    
#             else:  # 고슴도치 처리 (cell_type == 'S')
#                 if not visit[nx][ny] and (li[nx][ny] == '.' or li[nx][ny] == 'D'):
#                     visit[nx][ny] = True
#                     q.append((nx, ny, ctime + 1, 'S'))

# print("KAKTUS")

import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
li = []
for _ in range(R):
    li.append(list(input().strip()))

q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visit = [[False] * C for _ in range(R)]

# 물 먼저 큐에 넣기
for i in range(R):
    for j in range(C):
        if li[i][j] == '*':
            q.appendleft((i, j, 0))
        if li[i][j] == "S":
            q.append((i, j, 0))
            visit[i][j] = True

while q:
    cx, cy, ctime = q.popleft()
    
    # 고슴도치가 D에 도달했는지 체크 (이동하기 전에 체크)
    if li[cx][cy] == 'D':
        print(ctime)
        exit()

    # 4방향으로 퍼뜨리기
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny]:
            if li[cx][cy] == '*':  # 물 처리
                if li[nx][ny] == '.':  # 물은 빈 공간으로만 퍼짐
                    visit[nx][ny] = True
                    li[nx][ny] = '*'
                    q.append((nx, ny, ctime + 1))
                    
            elif li[cx][cy] == 'S':  # 고슴도치 처리
                if li[nx][ny] == '.' or li[nx][ny] == 'D':
                    visit[nx][ny] = True
                    if li[nx][ny] == '.':  # 빈 공간일 때만 S로 변경
                        li[nx][ny] = 'S'
                    # D일 때는 격자를 수정하지 않음
                    q.append((nx, ny, ctime + 1))

print("KAKTUS")