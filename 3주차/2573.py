import sys,copy
input=sys.stdin.readline
from collections import deque

n,m= map(int,input().split())

li= []
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for _ in range(n):
    li.append(list(map(int, input().split())))


def count_ice():
    cnt=0
    visit=[[False]* m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if li[i][j]>0 and not visit[i][j]:
                visit[i][j]=True
                bfs(i,j,visit)
                cnt+=1
    return cnt

def bfs(x,y,visit):
    q=deque()
    q.append((x,y))

    while q:
        cx,cy=q.popleft()
        
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]

            if(0<=nx<n and 0<=ny<m and not visit[nx][ny] and li[nx][ny]>0):
                visit[nx][ny]=True
                q.append((nx,ny))

def melt():
    global li
    li_copy=copy.deepcopy(li)

    for i in range(n):
        for j in range(m):
            if li_copy[i][j]>0:
                cnt=0
                for c in range(4):
                    nx=i+dx[c]
                    ny=j+dy[c]

                    if(0<=nx<n and 0<=ny<m and li_copy[nx][ny]==0):
                        cnt+=1
                li[i][j]=max(0, li_copy[i][j]-cnt) 

    
time=0

while(True):

    # if count_ice()>1:
    #     print(time)
    #     exit()

    # if count_ice()==0:
    #     print(0)
    #     exit()

    ice_count = count_ice()

    if ice_count>1:
        print(time)
        exit()
    
    if ice_count==0:
        print(0)
        exit()

    melt()
    time+=1


