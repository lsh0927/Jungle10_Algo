import sys
input= sys.stdin.readline


str1=input().strip()
str2=input().strip()

#dp는 str1의 i번째까지의 글자와 str2의 j번째 글자까지를 비교했을 때 LCS 
dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1 
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def LCS(x, y):
    # 기저 조건: 인덱스가 -1이면 0 반환
    if x == -1 or y == -1:
        return 0
    
    # 이미 계산된 값이 있으면 반환 (메모이제이션)
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 문자가 같으면 대각선 위 값 + 1
    if a[x] == b[y]:
        dp[x][y] = LCS(x-1, y-1) + 1
    else:
        # 문자가 다르면 위쪽과 왼쪽 중 최댓값
        dp[x][y] = max(LCS(x-1, y), LCS(x, y-1))
    
    return dp[x][y]

# 입력 받기
a = input().rstrip()
b = input().rstrip()

# DP 테이블 초기화 (-1로 초기화하여 미계산 상태 표시)
dp = [[-1 for _ in range(len(b))] for _ in range(len(a))]

# LCS 계산 및 출력
answer = LCS(len(a) - 1, len(b) - 1)
print(answer)