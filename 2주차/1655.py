import sys,math
input= sys.stdin.readline
import heapq as hq

N=int(input())

min_heap=[]
max_heap=[]

min_size=1
max_size=0

tmp=int(input())

hq.heappush(min_heap,-tmp)
print(tmp)

for i in range(1,N):
    num= int(input())

    # 길이 비교
    if min_size > max_size:
        if -min_heap[0] > num:
            hq.heappush(max_heap,-hq.heappop(min_heap))
            hq.heappush(min_heap,-num)
        else:
            hq.heappush(max_heap,num)
        max_size+=1
        
        print(-min_heap[0])

        #print(min_heap, max_heap)

    else:
        if max_heap[0] > num:
            hq.heappush(min_heap,-num)
        else:
            hq.heappush(min_heap,-hq.heappop(max_heap))
            hq.heappush(max_heap,num)            
        min_size+=1
        print(-min_heap[0])

        #print(min_heap, max_heap)
