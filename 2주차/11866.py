import sys,math
input= sys.stdin.readline

N,K= map(int, input().split())

idx = 0
queue = [i for i in range(1,N+1)]
res = []
while queue:
    idx += K-1
    if idx >= len(queue): 
        idx %= len(queue)
    res.append(str(queue.pop(idx)))

print("<", ", ".join(res), ">", sep="")
