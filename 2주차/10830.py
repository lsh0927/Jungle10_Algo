import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

N,B= map(int, input().split())
li=[]
for _ in range(N):
    li.append(list(map(int,input().split())))

MOD=1000

# 행렬의 제곱구현


def mul(A,B):
    n=len(A)
    matrix = [[0]* N for _ in range(N)]

    for row in range(n):
        for col in range(n):
            t=0
            for i in range(n):
                t+= A[row][i] * B[i][col]
            matrix[row][col]= t %1000

    return matrix




def sq(A,B):
    if B==1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %=1000
        return A

    tmp= sq(A,B//2)
    if B % 2:
        return mul(mul(tmp,tmp),A)
    else:
        return mul(tmp,tmp)



result= sq(li,B)

for val in result:
    print(*val)