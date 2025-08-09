import sys,math
input= sys.stdin.readline



K= int(input())
stack=[]
for _ in range(K):
    num= int(input())
    if num==0:
        if not stack:
            continue
        else:
            stack.pop()
    else: stack.append(num)

val=sum(stack)
print(val)