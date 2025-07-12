import sys,math
input= sys.stdin.readline

N= int(input())
li = []
for _ in range(N):
    li.append(list(map(int,input().split())))

min_val=1000000000
visited= [False]* N


def bt(start,cur,cost,depth):
    global min_val
    if depth==N-1:
        if li[cur][start] != 0:
            cost+=li[cur][start]
            min_val=min(cost,min_val)
        return

    for i in range(N):
        if not visited[i] and li[cur][i]>0:
            visited[i]=True
            bt(start,i,cost+li[cur][i],depth+1)
            visited[i]=False

for i in range(N):
    visited[i]=True
    bt(i,i,0,0)

print(min_val)