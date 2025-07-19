# import sys
# input = sys.stdin.readline

# M, N, L = map(int, input().split())
# slo = list(map(int, input().split()))  # 사대 위치들
# slo.sort()

# alo = []
# for i in range(N):
#     alo.append(tuple(map(int, input().split())))

# # 잡을 수 있는 동물 수 계산
# count = 0

# for animal in alo:
#     aj, bj = animal
#     can_catch = False
    
#     # 모든 사대에 대해 거리 계산
#     for xi in slo:
#         distance = abs(xi - aj) + bj
#         if distance <= L:
#             can_catch = True
#             break  
    
#     if can_catch:
#         count += 1

# print(count)

import sys
import bisect
input = sys.stdin.readline

M, N, L = map(int, input().split())
slo = list(map(int, input().split()))
slo.sort()

count = 0

for i in range(N):
    aj, bj = map(int, input().split())
    
    if bj > L:
        continue
    
    # 동물을 잡을 수 있는 사대의 범위 계산
    # |xi - aj| + bj <= L
    # |xi - aj| <= L - bj
    # aj - (L - bj) <= xi <= aj + (L - bj)
    
    max_distance = L - bj
    left_bound = aj - max_distance
    right_bound = aj + max_distance
    
    # 이진 탐색으로 범위 안에 있는 사대가 있는지 확인
    left_idx = bisect.bisect_left(slo, left_bound)
    right_idx = bisect.bisect_right(slo, right_bound)
    
    if left_idx < right_idx:  # 범위 안에 사대가 있으면
        count += 1

print(count)