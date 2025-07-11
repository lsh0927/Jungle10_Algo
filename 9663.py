import sys,math
input= sys.stdin.readline

N= int(input())

cols=[0] * N
ans=0


def check(r,c):
    for i in range(0,r):
        if(abs(r-i)==abs(cols[i]-c)): return False
        if(cols[i]==c): return False
    return True

    
def bt(idx):
    global ans
    if(idx==N):
        ans+=1
        return
    
    for i in range(0,N):
        if(check(idx,i)):
            cols[idx]=i
            bt(idx+1)

bt(0)
print(ans)