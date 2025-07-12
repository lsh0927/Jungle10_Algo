import sys,math
input= sys.stdin.readline


N=int(input())
li=list(map(int, input().split()))

max_val= max(li)
isPrime= [True]* (max_val+1)
isPrime[0]=isPrime[1]=False
cnt=0

for i in range(2,int(math.sqrt(max_val))+1):
    for j in range(i*i,max_val,i):
        isPrime[j]=False

for val in li:
    if isPrime[val]:
        cnt+=1

print(cnt)