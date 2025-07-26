import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

water_q = deque()
animal_q = deque()

visited = [[False] * C for _ in range(R)]


for y in range(R):
    for x in range(C):
        if grid[y][x] == '*':
            water_q.append((y, x))
        elif grid[y][x] == 'S':
            animal_q.append((y, x, 0))
            visited[y][x] = True

def spread_water():
    for _ in range(len(water_q)):
        y, x = water_q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            
            if grid[ny][nx] == '.':
                grid[ny][nx] = '*'
                water_q.append((ny, nx))

def move_animal_q():
    for _ in range(len(animal_q)):
        y, x, time = animal_q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            
            if grid[ny][nx] == 'D':
                return time + 1
            
            if grid[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                animal_q.append((ny, nx, time + 1))
    
    return -1

while animal_q:
    spread_water()
    
    result = move_animal_q()
    if result !=-1:
        print(result)
        exit()

print("KAKTUS")