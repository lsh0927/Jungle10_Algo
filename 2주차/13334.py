import sys
input = sys.stdin.readline
import heapq as hq

n= int(input())

li=[]

for _ in range(n):
    a,b=map(int, input().split())
    if a>b:
        li.append((b,a))
    else:
        li.append((a,b))

li.sort(key=lambda x: x[1])

L= int(input())

res =[]

max_val=0
for i in range(n):
    t_start= li[i][1]-L
    hq.heappush(res,li[i][0])
    while res and res[0] < t_start:
        hq.heappop(res)
    max_val=max(max_val,len(res))

print(max_val)
