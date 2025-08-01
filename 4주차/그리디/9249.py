# 메모리 초과 알고리즘 (이분탐색+해시)
# import sys
# input = sys.stdin.readline

# A = input().strip()
# B = input().strip()

# def find_lcs(A, B):
#     left, right = 0, min(len(A), len(B))
#     max_len = 0
#     result = ""
    
#     while left <= right:
#         mid = (left + right) // 2
#         found = False
        
#         # A의 길이 mid인 모든 부분 문자열을 집합에 저장
#         substrings = set()
#         for i in range(len(A) - mid + 1):
#             substrings.add(A[i:i + mid])
        
#         # B에서 길이 mid인 부분 문자열이 A에 있는지 확인
#         for i in range(len(B) - mid + 1):
#             substring = B[i:i + mid]
#             if substring in substrings:
#                 found = True
#                 result = substring
#                 break
        
#         if found:
#             max_len = mid
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return max_len, result

# max_len, result_string = find_lcs(A, B)
# print(max_len)
# if max_len > 0:
#     print(result_string)


import sys
input = sys.stdin.readline

def build_suffix_array(s):
    n = len(s)
    # 초기 순위: 각 문자의 ASCII 값
    rank = [ord(c) for c in s] + [0]  # 패딩
    
    sa = list(range(n))
    k = 1
    
    while k < n:
        # (rank[i], rank[i+k]) 기준으로 정렬
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else 0))
        
        # 새로운 rank 계산
        new_rank = [0] * (n + 1)

        # 첫번째는 무조건 rank 0 -> 구분용이기 때문?
        new_rank[sa[0]] = 0
        
        # for i in range(1, n):
        #     if (rank[sa[i]], rank[sa[i] + k] if sa[i] + k < n else 0) == \
        #        (rank[sa[i-1]], rank[sa[i-1] + k] if sa[i-1] + k < n else 0):
        #         new_rank[sa[i]] = new_rank[sa[i-1]]
        #     else:
        #         new_rank[sa[i]] = new_rank[sa[i-1]] + 1
        for i in range(1, n):
            if (rank[sa[i]], rank[sa[i] + k]) == (rank[sa[i-1]], rank[sa[i-1] + k]):
                new_rank[sa[i]] = new_rank[sa[i-1]]
            else:
                new_rank[sa[i]] = new_rank[sa[i-1]] + 1

        
        rank = new_rank
        k *= 2
    
    return sa

def build_lcp_kasai(s, sa):
    n = len(s)
    
    # rank 배열: sa의 역함수
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    
    lcp = [0] * n
    h = 0  # 현재 LCP 길이
    
    for i in range(n):
        if rank[i] > 0:  # 첫 번째가 아닌 경우
            j = sa[rank[i] - 1]  # 바로 앞 순서의 접미사 시작 위치
            
            # 이전에 계산한 h에서 최소 h-1만큼은 일치함을 활용
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            
            lcp[rank[i]] = h
            
            if h > 0:
                h -= 1  # 다음 계산을 위해 1 감소
    
    return lcp

A = input().strip()
B = input().strip()

# 두 문자열을 구분자로 연결
# '$'는 알파벳보다 사전순으로 앞에 와야 함
combined = A + '@' + B + '!'
n = len(combined)
len_A = len(A)

# 접미사 배열과 LCP 배열 구성
sa = build_suffix_array(combined)
lcp = build_lcp_kasai(combined, sa)

max_len = 0
result_string = ""

# LCP 배열을 순회하며 최장 공통 부분 문자열 찾기
for i in range(1, n):
    pos1 = sa[i-1]  # 이전 접미사의 시작 위치
    pos2 = sa[i]    # 현재 접미사의 시작 위치
    
    # 하나는 A에서, 하나는 B에서 온 접미사인지 확인
    # pos1 < len_A: A 문자열에서 온 접미사
    # pos2 > len_A: B 문자열에서 온 접미사 (구분자 '$' 이후)
    if (pos1 < len_A and pos2 > len_A) or (pos1 > len_A and pos2 < len_A):
        if lcp[i] > max_len:
            max_len = lcp[i]
            result_string = combined[pos1:pos1 + max_len]

print(max_len)
if max_len > 0:
    print(result_string)
else:
    print()