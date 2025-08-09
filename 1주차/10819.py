import sys,math
input= sys.stdin.readline

N= int(input())
li=list(map(int,input().split()))


max_val=0

def bt(idx,sum,arr,visited):
    global max_val
    
    if(idx==N):
        max_val=max(sum,max_val)
        return
    

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            arr[idx]=li[i]

            newSum= sum
            
            if idx>0:
                newSum+=abs(arr[idx-1]-arr[idx])
            bt(idx+1,newSum,arr,visited)
            visited[i]=False


bt(0,0, [0] * N, [False] *N)
print(max_val)

#위는 배치기반 접근

import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

max_val = 0

def bt(now, depth, sum):
    global max_val
    if depth == N:
        max_val = max(max_val, sum)
        return

    for next in range(N):  
        if not visited[next]:
            visited[next] = True
            diff = abs(li[now] - li[next])    
            bt(next, depth + 1, sum + diff)
            visited[next] = False

for i in range(N):
    visited = [False] * N
    visited[i] = True
    bt(i, 1, 0)  

print(max_val)

# 경로 기반도 있음
# IterTools.permutation
