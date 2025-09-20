# import sys
# input = sys.stdin.readline

# N,K = map(int, input().split())
# dp= [[0]*(K+1) for _ in range(N+1)]

# items=[]  
# for _ in range(N):
#     w,v = map(int, input().split())
#     items.append((w,v))

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         weight=items[i-1][0]  
#         value=itemsi-1][1]   
        
#         if j< weight:
#             dp[i][j]= dp[i-1][j]
#         else:
#             dp[i][j]= max(dp[i-1][j],dp[i-1][j-weight]+value)

# print(dp[N][K])

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())

    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[K])