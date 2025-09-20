import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def is_bipartite_bfs(graph,V):
    color= [-1] * (V+1)

    for start in range(1,V+1):
        # 첫 탐색
        if color[start]==-1:
            q= deque([start])
            color[start]=0

            while q:
                cur=q.popleft()
                for next in graph[cur]:
                    if color[next]==-1:
                        color[next]= 1-color[cur]
                        q.append(next)
                    elif color[next]==color[cur]:
                        return False

    return True            

K= int(input())
for _ in range(K):
    V,E= map(int,input().split())
    graph= [ [] for _ in range(V+1)]

    for _ in range(E):
        u,v= map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    print("YES" if is_bipartite_bfs(graph,V) else "NO")