import sys
input = sys.stdin.readline

N, K = map(int, input().split())
seq = list(map(int, input().split()))

multitap = set()
count = 0

for i in range(K):
    # 이미 꽂혀있으면 넘어감
    if seq[i] in multitap:
        continue
    
    # 멀티탭에 자리가 있으면 그냥 꽂음
    if len(multitap) < N:
        multitap.add(seq[i])
        continue
    
    # 멀티탭이 가득 찬 경우: 
    # 가장 나중에 사용되는 기기를 찾아서 뽑음
    latest_use = -1
    remove = -1
    
    for plugged in multitap:
        # 현재 꽂혀있는 기기가 앞으로 언제 사용되는지 찾음
        next_use = K  
        for j in range(i + 1, K):
            if seq[j] == plugged:
                next_use = j
                break
        
        # 가장 나중에 사용되는 기기를 찾음
        if next_use > latest_use:
            latest_use = next_use
            remove = plugged
    
    # 가장 나중에 사용되는 기기를 뽑고 새 기기를 꽂음  
    multitap.remove(remove)
    multitap.add(seq[i])
    count += 1

print(count)