import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

N= int(input())

stack= []

for _ in range(N):
    opList= list(map(str,input().split()))
    if opList[0]=="push":
        stack.append(int(opList[1]))
    elif opList[0]=="pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif opList[0]=="top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif opList[0]=="size":
        print(len(stack))
    else:
        if not stack:
            print(1)
        else:
            print(0)