import sys
input=sys.stdin.readline
from collections import deque

n,m= map(int,input().split())

li= []
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for _ in range(n):
    li.append(list(map(int,input().split())))


def bfs(i,j,visit):
    q=deque()
    q.append((i,j))
    visit[i][j]=True
    
    while q:
        cx,cy= q.popleft()

        for k in range(4):
            nx= cx+dx[k]
            ny= cy+dy[k]

            if(0<=nx<n and 0<=ny<m and not visit[nx][ny] and li[nx][ny]>0 ):
                visit[nx][ny]=True
                q.append((nx,ny))

def check():
    for i in range(n):
        for j in range(m):
            if li[i][j]>0:
                return False
    return True

def melt():
    new_li = [row[:] for row in li]  # 깊은 복사로 동시 녹이기
    
    for i in range(n):
        for j in range(m):
            if li[i][j]>0:
                cnt=0
                for x in range(4):
                    tx= i+dx[x]
                    ty= j+dy[x]

                    if(0<=tx<n and 0<=ty<m and li[tx][ty]==0):  # 경계 체크 추가
                        cnt+=1

                new_li[i][j]= max(0, li[i][j]-cnt)
    
    # 원래 배열에 복사
    for i in range(n):
        for j in range(m):
            li[i][j] = new_li[i][j]

def count_groups():
    visit=[ [False] * m for _ in range(n) ]  # 매번 새로 생성
    count=0
    
    for i in range(n):
        for j in range(m):
            if(li[i][j]>0 and not visit[i][j]):
                bfs(i,j,visit)
                count+=1
    return count

time=0

while(True):
    # 먼저 현재 상태에서 빙산 덩어리 개수 체크
    groups = count_groups()
    
    if groups >= 2:  # 2개 이상이면 현재 시간 출력
        print(time)
        break
    elif groups == 0:  # 모두 녹았으면 0 출력
        print(0)
        break
    
    # 1년 경과 (빙산 녹이기)
    melt()
    time+=1