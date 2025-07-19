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






# maxVal=0
# cnt=0
# total=0
# next_diff=0

# restart_point=0

# idx = 0
# while idx < N:
#     current_start = li[idx][0]
#     current_end = li[idx][1]


#     cur_length = current_end - current_start
#     if cur_length <= L:
#         cnt += 1
#     init_start = current_start
#     while True:
#         idx += 1
#         if idx == N:
#             break
#         next_start = li[idx][0]
#         next_end = li[idx][1]
#         if next_start < init_start:
#             continue
#         length = next_end - init_start
#         if length > L:
#             maxVal = max(maxVal, cnt)
#             cnt = 0

#             #현재 막대기에서 L만큼 뺀 지점을 찾아서 그 바로 앞 start를 init_start
#             restart_point=next_end - L


#             break
#         cnt += 1


# sys.stdout.write(str(maxVal))
    