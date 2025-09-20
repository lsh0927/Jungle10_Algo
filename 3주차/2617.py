import sys,math
input= sys.stdin.readline

N,M= map(int,input().split())

heavy= [[]for _ in range(N+1)]
light= [[]for _ in range(N+1)]

for _ in range(M):
    a,b= map(int,input().split())
    heavy[a].append(b)
    light[b].append(a)



def dfs(graph,cur):
    cnt=0
    for next in graph[cur]:
        if not visited[next]:
            visited[next]=True
            cnt+=1
            cnt+=dfs(graph,next)

    return cnt

mid=(N+1)//2


cnt=0

for i in range(1,N+1):
    visited= [False] * (N+1)
    if dfs(heavy,i)>=mid:
        cnt+=1
    if dfs(light,i)>=mid:
        cnt+=1

print(cnt)