import sys,math
input= sys.stdin.readline
import heapq as hq

N=int(input())

minHeap=[]
maxHeap=[]

li=[]

for _ in range(N):
    li.append(int(input()))

for i in range(N):

    if not minHeap:
        hq.heappush(minHeap, -li[i])

    else:
        # 중간값을 뽑아내야하므로, minHeap의 크기를 maxHeap크기 이상으로 맞춰야 함
        if len(minHeap) == len(maxHeap)+1:
            if li[i] >= -minHeap[0]:
                hq.heappush(maxHeap,li[i])
            else:
                hq.heappush(maxHeap, - (hq.heappop(minHeap)))
                hq.heappush(minHeap,-li[i])
        
        else:
            # 이번엔 maxHeap의 최소와 비교
            if li[i] > maxHeap[0]:
                hq.heappush(minHeap, - (hq.heappop(maxHeap)))
                hq.heappush(maxHeap, li[i])
            else:
                hq.heappush(minHeap, -li[i])

    print(-minHeap[0])