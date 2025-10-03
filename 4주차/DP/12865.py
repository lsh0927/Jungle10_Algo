import sys
input= sys.stdin.readline

N,K=map(int, input().split())

dp= [[0] * (K+1) for _ in range(N+1)]

li=[]

for _ in range(N):
    w,v= map(int,input().split())
    li.append((w,v))


for i in range(1,N+1):
    w=li[i-1][0]
    v=li[i-1][1]

    for weight in range(K+1):
        if weight<w:
            dp[i][weight]=dp[i-1][weight]

        else:
            dp[i][weight]=max(dp[i-1][weight], dp[i-1][weight-w]+v)

print(dp[N][K])

