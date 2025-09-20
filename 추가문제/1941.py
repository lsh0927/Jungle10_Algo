import sys,math
from collections import deque
input= sys.stdin.readline

li=[] 

for _ in range(5):
    li.append(input().rstrip())

ans=0

# 5*5로 구성이 완료됨
selected= [0] * 7

def isconnected(selected):

    # 동서남북 중 다른 하나와 이어져있다면? ㄴㄴ
    # 전부 인접해있으려면? 

    visit= [False] * 7
    q= deque()
    q.append(0)
    visit[0]=True

    cnt=1

    # 연쇄적으로 인접해있다의 의미
    
    while q:
        cur=q.popleft()
        cx,cy= selected[cur]

        # for i in range(1,7):
        #     if not visit[i]:
        #         tx,ty=selected[i]
        #         if abs(tx-cx)+abs(ty-cy)==1:
        #             visit[i]=True
        #             q.append(i)
        #             cnt+=1
        
        for i in range(1,7):
            if not visit[i]:
                tx,ty=selected[i]
                if abs(tx-cx) + abs(ty-cy) ==1:
                    visit[i]=True
                    q.append(i)
                    cnt+=1

    return cnt==7


def check(selected):
    cnt=0

    for r,c in selected:
        if(li[r][c]=='S'):
            cnt+=1

    return cnt>=4


def bt(idx,depth,selected):
    global ans
    if depth==7:
        if(isconnected(selected) and check(selected)):
            ans+=1
        return
    
    for i in range(idx,25):
        r,c=divmod(i,5)
        selected[depth]= (r,c)
        bt(i+1,depth+1,selected)

bt(0,0,selected)
print(ans)