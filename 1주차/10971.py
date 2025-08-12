import sys
input = sys.stdin.readline

N = int(input())

matrix= []
min_val= float('inf')

for _ in range(N):
    matrix.append(list(map(int,input().split())))

def bt(idx, cur, sum):
    global min_val
    if idx==N-1:
        if matrix[cur][0]!=0:
            sum+=matrix[cur][0]
            min_val=min(min_val,sum)
        return


    for i in range(N):
        if not visited[i] and matrix[cur][i]!=0:
            visited[i]=True    
            bt(idx+1,i,sum+matrix[cur][i])
            visited[i]=False

visited= [False] * N
visited[0]=True
bt(0,0,0)
print(min_val)