import sys,math
input= sys.stdin.readline

N= int(input())
li=list(map(int,input().split()))


max_val=0

def bt(idx,sum,arr,visited):
    global max_val
    if idx==N:
        max_val=max(max_val,sum)
        return
    
    #현재 idx와 그 전 idx의 값을 abs로 합 계산 한뒤 bt
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            tmp=sum
            arr[idx]=li[i]
            if idx>0:
                tmp+=abs[arr[idx]-arr[idx-1]]
            bt(idx+1,tmp,arr)
            visited[i]=False

visited= [False]*N

bt(0,0,[0]*N)
print(max_val)