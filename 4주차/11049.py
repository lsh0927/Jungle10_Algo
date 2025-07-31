import sys
input= sys.stdin.readline

N = int(input())
    
# dp[i][j]는 i~j구간의 최소 곱셈 횟수
dp = [[0] * N for _ in range(N)]
arr = []
    
for i in range(N):
    row, col = map(int, input().split())
    arr.append([row, col])
    

for d in range(N):
    for i in range(N-d):
        j=i+d
        dp[i][j]=float('inf')
        
        for k in range(i,j):
            dp[i][j]=min(dp[i][j], dp[i][k]+dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1])


print(dp[0][N-1])

