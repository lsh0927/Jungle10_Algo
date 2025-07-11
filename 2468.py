import sys,math
input= sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

mh = max(max(row) for row in arr)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y,h):
    isVisited[x][y]=True

    for i in range(0,4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if(nx>=0 and ny>=0 and nx<=n-1 and ny<=n-1 and not isVisited[nx][ny]): 
            if arr[nx][ny]>h:
                dfs(nx,ny,h)

    return 1

max_val = 0  # 초기화 추가

for t in range(0,mh):
    isVisited = [[False] * n for _ in range(n)]

    cnt=0
    #t 만큼의 장마가 내렸음
    for i in range(0,n):
        for j in range(0,n):
            # 높이 t 이하 지역은 물에 잠김
            if(not isVisited[i][j] and arr[i][j]>t):
                cnt+=dfs(i,j,t)

    max_val=max(max_val,cnt)

print(max_val)