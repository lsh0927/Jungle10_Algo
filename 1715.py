import sys,math
input= sys.stdin.readline
import heapq as hq
# sys.stdin.readline는 개행문자를 포함한채로 비교


N= int(input())

if N==1:
    print(0)
    sys.exit()

if N==2:
    tmp=0
    for _ in range(N):
        tmp+=int(input())
    print(tmp)
    sys.exit()

min_heap=[]

for i in range(N):
    hq.heappush(min_heap, int(input()))


total=0

while N>1:

    first= hq.heappop(min_heap)
    second= hq.heappop(min_heap)

    tmp2= first+second
    total+= tmp2

    hq.heappush(min_heap,tmp2) 
    
    N-=1
    if N==1:
        break

print(total)
