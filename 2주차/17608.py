import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

N= int(input())
stack=[]
for _ in range(N):
    stick= int(input())
    if not stack:
        stack.append(stick)
    else:
        while stack and stack[-1] <= stick:
            stack.pop()
        stack.append(stick)

print(len(stack))
# [9 7 6 4] 10