import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))


def bin_s(arr, target):

    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if arr[mid]< target:
            left= mid+1
        else:
            right=mid-1

    return left

res=[]

for num in li:
    sIdx= bin_s(res, num)

    if sIdx== len(res):
        res.append(num)
    else:
        res[sIdx]=num

print(len(res))

