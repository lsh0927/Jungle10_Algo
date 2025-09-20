import sys
input= sys.stdin.readline
import heapq as hq

T=int(input())

for _ in range(T):
    N=int(input())

    score=[]

    for _ in range(N):
        a,b= map(int,input().split())
        score.append((a,b))

    score.sort(key=lambda x: x[0])
    cnt=1
    cmp=[]
    hq.heappush(cmp,score[0][1])

    for i in range(1,N):
        if score[i][1] < cmp[0]:
            cnt+=1
            #print(i)
        hq.heappush(cmp, score[i][1])

    print(cnt)