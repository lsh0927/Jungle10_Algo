import sys
from collections import deque
input = sys.stdin.readline

def check(graph,V):
    # -1 => 방문하지 않음
    # 0 or 1 => 방문 후 색
    color=[-1] * (V+1)

    #  분리된 집합을 모두 검사
    for start in range(1,V+1):

        #미방문 노드
        if color[start]==-1:
            q=deque([start])
            color[start]=0
        
            while q:
                cur_node= q.popleft()

                for next in graph[cur_node]:
                    if color[next]== -1:
                        color[next] = 1- color[cur_node]
                        q.append(next)
                    else:
                        if color[next] == color[cur_node]:
                            return False
    
    return True






K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)] 
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if check(graph, V):
        print("YES")
    else:
        print("NO")