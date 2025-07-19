import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

tail = []

for num in li:
    pos = binary_search(tail, num)
    
    if pos == len(tail):
        tail.append(num)
    else:
        tail[pos] = num

print(len(tail))