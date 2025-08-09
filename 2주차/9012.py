import sys,math
input= sys.stdin.readline

T= int(input())

for _ in range(T):
    str=input().rstrip()
    # if str[0]==')' or str[len(str)-1]=='(':
    #     print("NO")
    #     continue

    stack=[]

    flag=True
    for c in str:
        if c=='(':
            stack.append(c)
        else:
            if not stack:
                flag=False
                break
            else:
                stack.pop()

    if flag and not stack:
        print("YES")
    else:
        print("NO")