import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교
# from queue import PriorityQueue

import heapq


N= int(input())
pq=[]

for _ in range(N):
    num= int(input())

    #0이면 비어있으면 0 , 차있으면 최댓값 출력 및 제거
    if num == 0:
        if not pq:
            print(0)
            continue
        else:
            print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq,-num)

