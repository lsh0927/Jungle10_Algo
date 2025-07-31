import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
dp = [0] * N

def recur(n):
    if dp[n] != 0:  
        return dp[n]
    
    dp[n] = 1  
    
    for i in range(n):  
        if li[i] < li[n]:
            dp[n] = max(dp[n], recur(i) + 1)
    
    return dp[n]

for i in range(N):
    recur(i)

print(max(dp))