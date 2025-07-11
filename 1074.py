import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def recur(n, row, col):
    if n == 0:
        return 0
    
    half = 2**(n-1)
    
    if row < half and col < half:
        # 1사분면 
        return recur(n-1, row, col)
    elif row < half and col >= half:
        # 2사분면
        return half * half + recur(n-1, row, col - half)
    elif row >= half and col < half:
        # 3사분면
        return 2 * half * half + recur(n-1, row - half, col)
    else:
        # 4사분면
        return 3 * half * half + recur(n-1, row - half, col - half)

print(recur(N, r, c))