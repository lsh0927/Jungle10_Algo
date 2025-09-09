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
    t,dir= map(str, input().split())
    change[int(t)]=dir


def isEnd(x,y):
    # 벽이나 자기 자신의 몸과 부딪히면 게임 끝
    if x<0 or x>=n or y<0 or y>=n:
        return True
    if (x,y) in q:
        return True
    return False

time=0
dir=0
# 우측부터 시계방향
dx=[0,1,0,-1]
dy=[1,0,-1,0]

q=deque()
q.append((0,0))

while(True):
    time+=1
    #cx,cy=q.popleft()
    cx,cy = q[0]



    nx=cx
    ny=cy

    if dir==0:
        ny+=1
    elif dir==1:
        nx+=1
    elif dir==2:
        ny-=1
    else : 
        nx-=1

    if isEnd(nx,ny):
        break

    if time in change:
        if change[time]=='D':
            dir= (dir+1)%4
        else:
            dir= (dir-1)%4
            if dir==-1:
                dir=3


    # if li[nx][ny]==1:
    #     # 사과가 있으면 꼬리가 줄어들지 않음
    #     q.appendleft((nx,ny))
    #     li[nx][ny]=0
    # else:
    #     q.appendleft((nx,ny))

    q.appendleft((nx,ny))
    if li[nx][ny]!=1:
        q.pop()
    else:
        li[nx][ny]=0
print(time)
