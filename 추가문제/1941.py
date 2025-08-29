import sys,math
from collections import deque
input= sys.stdin.readline

li=[] 

for _ in range(5):
    li.append(input().rstrip())

ans=0

dx= [0,1,0,-1]
dy= [1,0,-1,0]

def check(selected):
    cnt=0
    for i in range(7):
        cx,cy=selected[i]
        if li[cx][cy]=='S':
            cnt+=1
    if cnt>=4:
        return True
    return False

def isconnected(selected):
    # visited= [False]*25
    # sx,sy=selected[0]    
    # q= deque((sx,sy))
    # idx=1

    q=deque()
    q.append(0)
    visited=[False]* 7
    visited[0]=True

    
    cnt=1

    while q:
        cur= q.popleft()
        cx,cy=selected[cur]
        # visited[cx][cy]=True
        
        # for i in range(4):
        #     nx=cx+dx[i]
        #     ny=cy+dy[i]

        #     if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and selected[idx]:
        #         cnt+=1
        #         visited[nx][ny]=True
        #         q.append((nx,ny))

        for i in range(1,7):
            if not visited[i]:
                tx,ty=selected[i]
                if abs(cx-tx) +abs(cy-ty)==1:
                    visited[i]=True
                    q.append(i)
                    cnt+=1

    return (cnt==7)


def dfs(idx, depth, selected, str):
    global ans
    if depth==7:
        if isconnected(selected):
            if check(selected):
                ans+=1
        return

    for i in range(idx,25):
        r,c= divmod(i,5)
        selected[depth]=(r,c)
        dfs(i+1,depth+1,selected, str+li[r][c])

selected=[0]*7
dfs(0,0,selected,"")
print(ans)