import sys,math
from collections import deque
input= sys.stdin.readline

li = []

for _ in range(9):
    li.append(list(map(int,input().split())))

# 어떤식으로 구현할까
# idx(행)이 9에 도달하면 전체 검사를 하도록 ? ㄴㄴ
# 행 검사, 열 검사, 3x3 검사


def check(row,col,num):
    # 행 검사
    for i in range(9):
        if li[row][i]==num:
            return False
            
    for i in range(9):
        if li[i][col]==num:
            return False
        
    block_row= (row//3)*3
    block_col= (col//3)*3

    for r in range(block_row, block_row + 3):
        for c in range(block_col, block_col + 3):
            if li[r][c] == num:
                return False
    return True

def dfs(row,col):
    if row==9:
        for i in range(9):
            print(*li[i])
        sys.exit(0)
        return
    
    if col==9:
        dfs(row+1,0)
        return

    if li[row][col]!=0:
        dfs(row,col+1)
        return

    for num in range(1,10):
        if check(row,col,num):
            li[row][col]=num
            dfs(row,col+1)
            li[row][col]=0

dfs(0,0)
