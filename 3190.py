import sys,math
input= sys.stdin.readline

from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    a,b= map(int,input().split())
    board[a-1][b-1]=1

l= int(input())

direction_change={}
for _ in range(l):
    line= input().split()
    x= int(line[0])
    c=line[1]
    #put의 역할?
    direction_change[x]=c

dx=[0, 1, 0, -1] 
dy=[1, 0, -1, 0]

snake=deque([(0,0)])

cx,cy=0,0
time=0
direction=0

def isFin(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return True
    
    if (x,y) in snake:
        return True
    
    return False



while True:

    # 시간 증가
    time+=1

    # 한칸 전진
    nx=cx+dx[direction]
    ny=cy+dy[direction]

    #종료조건이면 탈출
    if isFin(nx,ny):
        break

    # 사과있으면 0 변환 + 길이 증가
    if board[nx][ny]==1:
        board[nx][ny]=0
        snake.append((nx,ny))

    # 사과없으면 길이 추가후 이전 몸통 제거
    else:
        snake.append((nx,ny))
        snake.popleft()

    if time in direction_change:
        if direction_change[time] == "D":
            direction = (direction + 1) % 4
        else:  # "L"
            direction = (direction - 1) % 4
    
    cx=nx
    cy=ny

print(time)
