import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교
from collections import deque
import heapq as hq

class Node:
    def __init__(self,to,cost):
        self.to=to
        self.cost=cost
        
 
N= int(input())
M= int(input())
graph= [ [] for _ in range(N+1)]
visited= [False] * (N+1)

for _ in range(M):
    start,end,cost= map(int,input().split())
    graph[start].append(Node(end,cost))

A,B= map(int,input().split())
dist= [float('inf') for _ in range(N+1)]
dist[A]=0

pq=[(0,A)]


def dijk():

    while pq:
        cur_cost, cur_node= hq.heappop(pq)
    
        if cur_cost> dist[cur_node]:
            continue

        if cur_node==B:
            return cur_cost

        for next in graph[cur_node]:
            next_node= next.to
            next_cost= next.cost+cur_cost

            if next_cost< dist[next_node]:
                dist[next_node]=next_cost
                hq.heappush(pq,(next_cost,next_node))

print(dijk())

    