import sys
input= sys.stdin.readline
from collections import deque
import heapq as hq

n=int(input())
dp= [0] * (n+1)

if n >= 0:
    dp[0] = 0
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 1

for i in range(3, n+1):  
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])