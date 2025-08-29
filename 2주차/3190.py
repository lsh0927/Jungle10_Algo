import sys,math
input= sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

li = [[0] * n for _ in range(n)]

for _ in range(k):
    r,c= map(int,input().split())
    li[r-1][c-1]=1

l= int(input())
change={}

for _ in range(l):
    line= input().split()
    x= int(line[0])
    c=line[1]
    change[x]=c

dx=[0, 1, 0, -1] 
dy=[1, 0, -1, 0]

q=deque([(0,0)])

cx,cy=0,0
time=0
dir=0

def isEnd(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return True
    
    if (x,y) in q:
        return True
    
    return False


while True:
    time+=1

    nx=cx+dx[dir]
    ny=cy+dy[dir]

    if isEnd(nx,ny):
        break

    if li[nx][ny]==1:
        li[nx][ny]=0
        q.append((nx,ny))

    else:
        q.append((nx,ny))
        q.popleft()

    if time in change:
        if change[time] == "D":
            dir = (dir + 1) % 4
        else: 
            dir = (dir - 1) % 4
    
    cx=nx
    cy=ny

print(time)
