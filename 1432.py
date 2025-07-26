import heapq
import sys

input = sys.stdin.readline

def topology_sort():
  q = []
  for i in range(1, n+1):
    if indegree[i] == 0:
      # heapq.heappush(q,i)
      heapq.heappush(q,-i)
  
  N = n
  while q:
    now = -heapq.heappop(q)
    answer[now] = N
    
    for i in node[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        heapq.heappush(q, -i)
    N -=1

n = int(input())
node = [[] for _ in range((n+1))]
indegree = [0] * (n+1)

# 인접행렬 입력 ->인접리스트로 변경
for v in range(1, n+1):
  # temp[1] 부터 실행하기 위함
  # n = 3, 입력:
  # 0 1 0  ← 1번째 행: 2번이 1번으로 들어옴 (2→1)
  # 1 0 1  ← 2번째 행: 1번과 3번이 2번으로 들어옴 (1→2, 3→2) 
  # 0 1 0  ← 3번째 행: 2번이 3번으로 들어옴 (2→3)

  # 변환:
  # v=1, temp=[0,0,1,0] → temp[2]=1 → 2에서 1로 → node[2].append(1)
  # v=2, temp=[0,1,0,1] → temp[1]=1 → 1에서 2로 → node[1].append(2)
        # → temp[3]=1 → 3에서 2로 → node[3].append(2)
        # v=3, temp=[0,0,1,0] → temp[2]=1 → 2에서 3으로 → node[2].append(3)
  temp = [0]+ list(map(int, input().strip()))
  for i in range(1, n+1):
    if temp[i] == 1:
      node[i].append(v)
      indegree[v] += 1

answer = [0]*(n+1)

topology_sort()
if answer.count(0) > 1:
  print(-1)
else:
  print(*answer[1:])