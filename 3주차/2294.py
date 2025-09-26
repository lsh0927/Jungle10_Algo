import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
   coins.append(int(input()))

coins= list(set(coins))

# #BFS
# visited = [False] * (k + 1)
# visited[0] = True
# q=deque()

# for coin in coins:
#    q.append((coin,1))

# while q:
#    cur, cnt= q.popleft()
   
#    if cur>k:
#       continue

#    if cur==k:
#       print(cnt)
#       exit()
   
#    for coin in coins:
#       if(cur+coin <=k and not visited[cur+coin]):
#         visited[cur+coin]=True
#         q.append((cur+coin,cnt+1))

# print(-1)

#dp

dp=[float('inf')] * (k+1)
dp[0]=0
for coin in coins:
    for i in range(coin,k+1):
        # if dp[i-coin] != float('inf'):
            dp[i]=min(dp[i], dp[i-coin]+1)

if dp[k]== float('inf'):
    print(-1)
else:
    print(dp[k])        

