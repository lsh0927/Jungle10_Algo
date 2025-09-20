import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
li=[]

for _ in range(N):
    li.append(list(map(int, input().split())))

max_val=1
max_height = max(max(row) for row in li)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(r,c,height):

    q= deque()
    q.append((r,c))

    visit[r][c]=True

    while q:
        curX,curY=q.popleft()

        for i in range(4):
            nx=curX+dx[i]            
            ny=curY+dy[i]            

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny] and li[nx][ny]>height:
                visit[nx][ny]=True
                q.append((nx,ny))


#0부터 N-1까지 높이로 BFS 설정
for i in range(max_height+1):
    visit=[ [False] * N for _ in range(N) ]
    cnt=0
    for r in range(N):
        for c in range(N):
            if not visit[r][c] and li[r][c]>i:
                bfs(r,c,i)
                cnt+=1

    max_val=max(max_val,cnt)

print(max_val)