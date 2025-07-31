import sys
input = sys.stdin.readline
from collections import deque

N,M=map(int,input().split())

small=set()

for _ in range(M):
    small.add(int(input()))

dp= [ [float('inf')] * (int((2*N) ** 0.5) +2) for _ in range(N+1)]
dp[1][0]=0

for i in range(2, N+1):
    if i in small:
        continue
    for j in range(1, int((2*i)**0.5)+1):
        dp[i][j]= min(dp[i-j][j-1], dp[i-j][j],dp[i-j][j+1])+1

if min(dp[N])==float('inf'):
    print(-1)
else:
    print(min(dp[N]))





# check= [ [] for _ in range(N+1)]
# def bfs():
#     q=deque([(1,0,0)])

#     while q:
#         cur,jump,cnt= q.popleft()

#         for x in [jump, jump-1,jump+1]:
#             if x>0:
#                 next=cur+x
#                 if next==N:
#                     return cnt+1
#                 if next<N and next not in small and x not in check[next]:
#                     check[next].append(x)
#                     q.append((next,x,cnt+1))

#     return -1
# print(bfs())