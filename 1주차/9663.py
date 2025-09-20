import sys
input = sys.stdin.readline

N=int(input())
cols = [0] * N  
cnt=0

def check(r,c):
    for i in range(r):
        if cols[i]==c: return False
        if abs(i-r)==abs(cols[i]-c) : return False
    return True

def bt(idx):
    global cnt
    if idx==N:
        cnt+=1
        return
    
    for i in range(N):
        if check(idx,i):
            cols[idx]=i
            bt(idx+1)


bt(0)
print(cnt)