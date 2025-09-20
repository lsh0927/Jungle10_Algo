import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

li.sort()

start = 0
end = N - 1
min_sum = float('inf')
result = (0, 0)

while start < end:  
    current_sum = li[start] + li[end]
    
    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        result = (li[start], li[end])
    
    if current_sum == 0:
        break
    elif current_sum < 0:
        start += 1  
    else:
        end -= 1    

print(result[0], result[1])