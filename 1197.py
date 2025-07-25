import sys
input= sys.stdin.readline
import heapq as hq

V,E= map(int,input().split())

# 크루스칼에서 사용할 리스트
edges=[]

for _ in range(E):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

# cost가 적은것부터 정렬
edges.sort(key=lambda x: x[2])

# 유니온 파인드
parent= [i for i in range(V+1)]

def find(x):
    if(parent[x]==x):
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    pa,pb= find(a),find(b)  
    if pa<pb:
        parent[pb]=pa
    else:
        parent[pa]=pb

answer=0

for a,b,cost in edges:
    if find(a)!=find(b):
        union(a,b)
        answer+=cost

print(answer)