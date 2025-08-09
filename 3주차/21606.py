from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N= int(input())
str= input().rstrip()

status=[0] * (N+1)
for i in range(1,len(str)+1):
    if str[i-1]=='1':
        status[i]=1
cnt=0
graph= [ [] for _ in range(N+1)]
for _ in range(N-1):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    if status[a]==1 and status[b]==1:
        cnt+=2

visited= set()

def dfs(cur):
    indoor=0
    
    for next in graph[cur]:
        if status[next]==0:
            if next not in visited:
                visited.add(next)
                indoor+=dfs(next)
        else:
            indoor+=1
    
    return indoor





for i in range(1,N+1):
    indoor=0
    if status[i]==0:
        if i not in visited:
            visited.add(i)
            indoor= dfs(i)
    cnt+= indoor*(indoor-1)
            
print(cnt)