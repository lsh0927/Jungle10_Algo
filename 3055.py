import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque()
visited = [[False] * C for _ in range(R)]

# 같은 시간이라면 물을 먼저 처리하기 위해 물을 먼저 큐에 추가
for y in range(R):
    for x in range(C):
        if grid[y][x] == '*':
            queue.append((0, 'water', y, x))  # (시간, 타입, y, x)

for y in range(R):
    for x in range(C):
        if grid[y][x] == 'S':
            queue.append((0, 'animal', y, x))
            visited[y][x] = True

while queue:
    time, entity_type, y, x = queue.popleft()
    
    if entity_type == 'water':
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '.':
                grid[ny][nx] = '*'
                queue.append((time + 1, 'water', ny, nx))
    
    else: 
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < R and 0 <= nx < C:
                if grid[ny][nx] == 'D':
                    print(time + 1)
                    exit()
                
                if grid[ny][nx] == '.' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((time + 1, 'animal', ny, nx))

print("KAKTUS")