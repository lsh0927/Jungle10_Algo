import sys,math
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
ta, ts, tm, td = map(int, input().split())

max_val = float('-inf')
min_val = float('inf')

def dfs(idx, cur, ra, rs, rm, rd):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, cur)
        min_val = min(min_val, cur)
        return

    if ra > 0:
        dfs(idx+1, cur + li[idx], ra-1, rs, rm, rd)
    if rs > 0:
        dfs(idx+1, cur - li[idx], ra, rs-1, rm, rd)    
    if rm > 0:
        dfs(idx+1, cur * li[idx], ra, rs, rm-1, rd)  
    if rd > 0:
        # 나눗셈 처리 (음수 나눗셈은 0쪽으로)
        if cur < 0:
            dfs(idx+1, -(-cur // li[idx]), ra, rs, rm, rd-1)
        else:
            dfs(idx+1, cur // li[idx], ra, rs, rm, rd-1)

dfs(1, li[0], ta, ts, tm, td)
print(max_val)
print(min_val)