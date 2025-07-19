import sys
input = sys.stdin.readline

N= int(input())
n=0
li=[]

if N==0:
    print(1)
else:
    cnt=0
    a=N//10
    b=N%10

    li.append(str(N))
    while N!=n:
        n=10*b +((a+b)%10)
        cnt+=1
        a=n//10
        b=n%10
    print(cnt)
