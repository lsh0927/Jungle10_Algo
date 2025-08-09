import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

N=int(input())
li= list(map(int,input().split()))

stack=[]
res=[0] * N

# [6 9 6 7 4]
# [0] 1
# li[stack[-1]] 와 li[1] 비교해서 li[1]가 크거나 같다?
# 그럼 수신할 탑이 나올때까지 같거나 작은 탑의 인덱스를 pop하고, 끝까지 가도 없다면 res[i]는 0이 됨
# 만약 li[1]가 더 작다면? stack[-1]가 res[i]가 될것

# 스택에는 뭐가 들어가지 -> list와 비교했을 때, 원소와 stack의 top을 비교해서 큰걸 찾을때까지 pop이 필요
# 즉 스택에는 인덱스가 들어가야 맞음

# 리스트에는 탑의 높이가 있음
# 결과로 수신하는 탑의 번호, 인덱스를 써야 함

for i in range(N):
    if i==0:
        stack.append(i)
        res[0]=0
    
    while stack and li[stack[-1]] <= li[i]:
        stack.pop()
    
    if not stack:
        stack.append(i)
        res[i]=0
    else:
        res[i]=stack[-1]+1
        stack.append(i)


for val in res:
    print(val , end=' ')