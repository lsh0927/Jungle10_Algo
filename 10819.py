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