# from collections import deque
# def solution(priorities, location):
    
    
#     q=deque()
    
#     for i in range(len(priorities)):
#         q.append((i,priorities[i]))
    
#     max_pri= max(priorities)
#     seq=1
#     while q:
#         cur_idx,cur_pri=q.popleft()
#         if cur_pri==max_pri:
#             if cur_idx==location:
#                 return seq
#             else:
#                 #우리가 원하는 location이 아니면 순서만 1증가
#                 seq+=1
                
#                 priorities.remove(max_pri)
#                 max_pri=max(priorities)
#                 # max 초기화
                
#         else:
#             q.append((cur_idx,cur_pri))
                
                
#     return seq

from collections import deque, Counter

def solution(priorities, location):
    q = deque()
    
    # (인덱스, 우선순위) 쌍으로 큐 구성
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    # 우선순위별 개수를 Counter로 관리
    priority_count = Counter(priorities)
    
    # 정렬된 우선순위 리스트 (내림차순)
    sorted_priorities = sorted(priority_count.keys(), reverse=True)
    current_max_idx = 0  # 현재 처리 중인 최대 우선순위의 인덱스
    
    seq = 0
    
    while q:
        cur_idx, cur_pri = q.popleft()
        current_max = sorted_priorities[current_max_idx]
        
        if cur_pri == current_max:
            seq += 1
            if cur_idx == location:
                return seq
            
            # 해당 우선순위 개수 감소
            priority_count[cur_pri] -= 1
            
            # 해당 우선순위를 모두 처리했으면 다음 우선순위로 이동
            if priority_count[cur_pri] == 0:
                current_max_idx += 1
        else:
            q.append((cur_idx, cur_pri))
    
    return seq