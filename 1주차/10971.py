# import sys,math
# input= sys.stdin.readline

# N= int(input())
# li = []
# for _ in range(N):
#     li.append(list(map(int,input().split())))

# min_val=1000000000
# visited= [False]* N


# def bt(start,cur,cost,depth):
#     global min_val
#     if depth==N-1:
#         if li[cur][start] != 0:
#             cost+=li[cur][start]
#             min_val=min(cost,min_val)
#         return

#     for i in range(N):
#         if not visited[i] and li[cur][i]>0:
#             visited[i]=True
#             bt(start,i,cost+li[cur][i],depth+1)
#             visited[i]=False

# for i in range(N):
#     visited[i]=True
#     bt(i,i,0,0)

# print(min_val)

import sys
input = sys.stdin.readline

N = int(input())
min_val = float('inf')

cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

def bt(start, now, depth, current_sum):
    global min_val
    
    # 가지치기: 현재 비용이 이미 최소값보다 크면 종료
    if current_sum >= min_val:
        return
    
    if depth == N - 1:
        if cost[now][start] > 0:
            total_cost = current_sum + cost[now][start]
            min_val = min(total_cost, min_val)
        return
    
    for i in range(N):
        if not visited[i] and cost[now][i] > 0:
            visited[i] = True
            bt(start, i, depth + 1, current_sum + cost[now][i])
            visited[i] = False

# 시작점 0에서만 시작 (대칭성 이용)
# TSP는 원형 경로를 찾는 문제이므로 한 군데에서만 시작해도 됨
visited = [False] * N
visited[0] = True
bt(0, 0, 0, 0)

print(min_val)

