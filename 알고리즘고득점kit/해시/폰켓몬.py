from collections import defaultdict
def solution(nums):
    
    answer= min(len(nums)//2,len(set(nums)))
    return answer

# 키 개수
#len(hash_dict)           # 3
# 값들의 합 (전체 원소 개수)
#sum(hash_dict.values())  # 8
# 가장 많이 나온 값
#max(hash_dict.values())  # 3