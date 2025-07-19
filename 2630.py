import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

total_white = 0
total_blue = 0

def check(length, r, c):
    if length == 1:
        return li[r][c]
    
    white = 0
    blue = 0
    
    for i in range(r, r + length):
        for j in range(c, c + length):
            if li[i][j] == 1:
                blue += 1
            else:
                white += 1
    
    if blue != 0 and white != 0:
        return 2  
    elif white == length * length:
        return 0  
    else:
        return 1  

def recur(n, r, c):
    global total_white, total_blue
    
    result = check(n, r, c)
    
    if result == 2:  
        half = n // 2
        recur(half, r, c)
        recur(half, r + half, c)
        recur(half, r, c + half)
        recur(half, r + half, c + half)
    elif result == 1: 
        total_blue += 1
    else:  
        total_white += 1

recur(N, 0, 0)

print(total_white)
print(total_blue)