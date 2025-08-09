import sys,math
input= sys.stdin.readline
import heapq as hq

N = int(input())
li= []

for _ in range(N):
    a,b= map(int, input().split())
    if a>b:
        li.append((b,a))
    else:
        li.append((a,b))
    
L= int(input())
li.sort(key=lambda x : (x[1],x[0]))


min_heap=[]
max_cnt=0
for lo in li:
    start,end=lo
    hq.heappush(min_heap,start)
    t_start= end - L
    while min_heap and min_heap[0] < t_start:
        hq.heappop(min_heap)
    max_cnt=max(max_cnt, len(min_heap))    

print(max_cnt)