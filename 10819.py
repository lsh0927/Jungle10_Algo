import sys,math
input= sys.stdin.readline

N= int(input())
li= list(map(int, input().split()))

max_val=0
def bt(idx,sum,arr,used):
    global max_val
    if idx==N:
        max_val=max(max_val,sum)
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            arr[idx] = li[i]
            new_sum = sum
            if idx > 0:
                new_sum += abs(arr[idx-1] - arr[idx])
            bt(idx+1,new_sum,arr,used)
            used[i] = False

bt(0,0,[0]*N,[False]*N)
print(max_val)