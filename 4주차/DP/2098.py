import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(cur, visited):
    # 모든 도시를 방문했다면
    if visited == (1 << N) - 1:
        if matrix[cur][0] != 0:
            return matrix[cur][0]
        else:
            return float('inf')
    
    # 이미 계산된 값이 있다면 반환
    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    # 최소값을 찾기 위해 무한대로 초기화
    dp[cur][visited] = float('inf')
    
    # 다음 도시들을 탐색
    for next_city in range(N):
        # 현재 도시에서 next_city로 갈 수 없거나, 이미 방문한 도시라면 스킵
        if matrix[cur][next_city] == 0 or (visited & (1 << next_city)):
            continue
        
        # 다음 도시로 가는 비용 + 그 이후의 최소 비용
        cost = matrix[cur][next_city] + dfs(next_city, visited | (1 << next_city))
        dp[cur][visited] = min(dp[cur][visited], cost)
    
    return dp[cur][visited]

print(dfs(0, 1))