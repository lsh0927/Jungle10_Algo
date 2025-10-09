# answer = -1

# def DFS(n, pos, num, number):
#     global answer
#     if pos > 8:
#         return
#     if num == number:
#         if pos < answer or answer == -1:
#             answer=pos
#         return

#     nn=0
#     for i in range(8):
#         nn=nn*10+n
#         DFS(n, pos+1+i, num+nn, number)
#         DFS(n, pos+1+i, num-nn, number)
#         DFS(n, pos+1+i, num*nn, number)
#         DFS(n, pos+1+i, num/nn, number)

# def solution(N, number):    
#     DFS(N, 0, 0, number)    
#     return answer

def solution(N, number):
    if N == number:
        return 1
    
    # dp[i] = N을 i번 사용해서 만들 수 있는 수들
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 1. N을 i번 연속으로 붙인 수
        dp[i].add(int(str(N) * i))
        
        # 2. 이전 결과들을 조합
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        # 3. number를 찾으면 반환
        if number in dp[i]:
            return i
    
    return -1