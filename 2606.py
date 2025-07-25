import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

V=int(input())
E=int(input())

parent= [i for i in range(V+1)]

def find(a):
    if parent[a]==a:
        return a
    
    parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    pa=find(a)
    pb=find(b)

    if pa<pb:
        parent[pb]=pa
    else:
        parent[pa]=pb

for _ in range(E):
    start,end= map(int,input().split())
    if find(start)!=find(end):
        union(start,end)

cmp=find(1)
cnt=0
for i in range(2,V+1):
    if find(i)==cmp:
        cnt+=1

print(cnt)