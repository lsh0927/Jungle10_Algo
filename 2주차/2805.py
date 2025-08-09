import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

max_height = max(li)
left = 0
right = max_height-1  
answer = 0  

while left <= right:
    mid = (left + right) // 2
    
    remain = 0
    for val in li:
        if val > mid:
            remain += val - mid
    
    if remain >= M:  
        answer = mid  
        left = mid + 1  
    else:
        right = mid - 1

print(answer)