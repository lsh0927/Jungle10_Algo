import sys,math
input= sys.stdin.readline

N,M= map(int,input().split())

heavy= [[]for _ in range(N+1)]
light= [[]for _ in range(N+1)]

for _ in range(M):
    h,l= map(int,input().split())
    heavy[h].append(l)
    light[l].append(h)

def dfs(li,cur):
    cnt=0

    for next in li[cur]:
        if not visited[next]:
            visited[next]=True
            cnt+=1
            cnt+=dfs(li,next)
    return cnt
    
    
mid = (N+1)/2
result = 0

for i in range(1,N+1):
    visited=[False] *(N+1)
    if dfs(heavy,i) >= mid:
        result+=1
    if dfs(light,i) >= mid:
        result+=1

print(result)