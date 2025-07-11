import sys,math
input= sys.stdin.readline

N= int(input())

# 각 자리가 등차 수열?

# 1~99 -> o
# 100 이상 -> 리스트를 반복문으로 순회

if N <100:
    print(N)
else:
    cnt = 99 
    for i in range(100, N+1):
        li=[]

        while(i>0):
            li.append(i%10)
            i//=10
        
        li.reverse()
        isTrue=True

        diff= li[1]-li[0]
        
        for val in range(2,len(li)):
            if li[val]-li[val-1] != diff:
                isTrue=False
                break
        if isTrue:
            cnt+=1
    print(cnt)