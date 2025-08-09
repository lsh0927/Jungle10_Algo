import sys,math
input= sys.stdin.readline

N= int(input())

for _ in range(N):
    str= input()

    score=0
    cons=0
    if str[0]=='O':
        score+=1
        cons+=1
    
    for i in range(1,len(str)):
        if(str[i]=='O'):
            cons+=1
            score+=cons
        else:
            cons=0

    print(score)