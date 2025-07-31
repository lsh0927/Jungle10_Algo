import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

N=int(input())
isIndoor= input().strip()

status= [0] * (N+1)

for i in range(1,len(isIndoor)+1):
    if isIndoor[i-1]=='1':
        status[i]=1


cnt=0
graph= [ [] for _ in range(N+1)]

for _ in range(N-1):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

    if status[a]==1 and status[b]==1:
        cnt+=2

visited= [False] * (N+1)

def dfs(cur):
    indoor=0

    for next in graph[cur]:
        if status[next]==0:
            if not visited[next]:
                visited[next]=True
                indoor+=dfs(next)
        else:
            indoor+=1
    return indoor

for i in range(1,N+1):
    indoor=0
    if status[i]==0:
        if not visited[i]:
            visited[i]=True
            indoor=dfs(i)

    cnt+=indoor*(indoor-1)

print(cnt)