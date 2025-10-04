from collections import defaultdict
def solution(participant, completion):
    
    hash_dict=defaultdict(int)
    
    for part in participant:
        hash_dict[part]+=1
    
    for per in completion:
        hash_dict[per]-=1
    
    
    for key,val in hash_dict.items():
        if val>0:
            return key