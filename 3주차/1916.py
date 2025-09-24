import sys
input= sys.stdin.readline
#from collections import deque
import heapq as hq

MAX= 9999999999 

N=int(input())
M=int(input())

graph= [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))

dist=[MAX] * (N+1)

start,end= map(int,input().split())
dist[start]=0

q=[]
# 큐에 처음으로 넣을 값?
hq.heappush(q,(0,start))

def dijk():

    while q:
        curCost, curNode=hq.heappop(q)

        if curCost> dist[curNode]:
            continue
        
        for nextNode, nextCost in graph[curNode]:
            newCost= dist[curNode]+ nextCost

            if newCost < dist[nextNode]:
                dist[nextNode]=newCost
                hq.heappush(q,(newCost,nextNode))    


dijk()
print(dist[end])