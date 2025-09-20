import sys
input= sys.stdin.readline
import heapq as hq

sys.getrecursionlimit(100000)

V,E= map(int,input().split())

#li= [[V+1] for _ in range[V+1]]
edges=[]

for _ in range(E):
    a,b,cost= map(int,input().split()) 
    #li[a].append((b,cost))
    edges.append((a,b,cost))

edges.sort(key=lambda x:x[2])

# 유니온 파인드
parent= [i for i in range(V+1)]
answer=0
def find(a):
    if(parent[a]==a):
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
    
def union(a,b):
    pa=find(a)
    pb=find(b)

    if(pa>pb):
        parent[pb]=pa
    else:
        parent[pa]=pb

for a,b,cost in edges:
    if(find(a)!=find(b)):
        union(a,b)
        answer+=cost

print(answer)
