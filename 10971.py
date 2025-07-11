import sys,math
input= sys.stdin.readline


N= int(input())
li=[]
for _ in range(N):
    li.append(list(map(int, input().split())))

visited= [False]* N
ans= 1000000000

def dfs(start, now , depth, sum):
    global ans
    if depth==N-1:
        if li[now][start] != 0:
            sum+= li[now][start]
            ans = min(ans,sum)
        return

    for i in range(0,N):
        if(not visited[i] and li[now][i]>0):
            visited[i]=True
            dfs(start,i,depth+1,sum+li[now][i])
            visited[i]=False

for i in range(0,N):
    visited[i]=True
    dfs(i,i,0,0)

print(ans)