import sys
input= sys.stdin.readline


N,K= map(int,input().split())

val=[]

for _ in range(N):
    val.append(int(input()))

val.reverse()

idx=0
cnt=0
total=0
while True:

    if total+val[idx]>K:
        idx+=1
        continue

    if total+val[idx]==K:
        print(cnt+1)
        sys.exit()
    
    else:
        total+=val[idx]
        cnt+=1
    
    