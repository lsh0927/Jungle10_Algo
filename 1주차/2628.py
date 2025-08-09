import sys,math
input= sys.stdin.readline

R,C= map(int, input().split())

T=int(input())

row=[0,C]
col=[0,R]

for _ in range(T):
    type, num= map(int, input().split())
    if type==0:
        row.append(num)
    else:    
        col.append(num)
        

row.sort()
col.sort()

max_c=0
max_r=0

for i in range(1,len(row)):
    max_c= max(max_c,row[i]-row[i-1])

for i in range(1,len(col)):
    max_r= max(max_r,col[i]-col[i-1])

print(max_r*max_c)