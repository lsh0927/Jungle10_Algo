import sys,math
input= sys.stdin.readline

N= int(input())
li= list(map(int,input().split()))


x=max(li)

cnt=0

isPrime=[True]*(x+1)
isPrime[0]=isPrime[1]=False

#에라토스테네스의 체
def ert():
    for i in range(2, int(math.sqrt(x))+1):
        if isPrime[i]:
            for j in range(i*i,x+1, i):
                isPrime[j]=False
    
ert()

for val in li:
    if isPrime[val]:
        cnt+=1

print(cnt)

