from collections import defaultdict
def solution(clothes):
    
    # 각 key에 해당하는 (value+1)을 해서, 각 value를 모두 곱한뒤 -1 
    
    hash_dict= defaultdict(int)
    
    for t, cloth in clothes:
        hash_dict[cloth] +=1
        
    answer = 1
        
    for key, val in hash_dict.items():
        answer*=(val+1)
    
    return answer-1