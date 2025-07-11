import sys,math
input= sys.stdin.readline

T= int(input())

def isPrime(n):
    if(n<=1): return False
    if(n==2): return True
    if(n%2==0): return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if(n%i==0):
            return False
    return True

for _ in range(T):
    n= int(input())

    left=n//2
    right=n//2

    while(not isPrime(left) or not isPrime(right)):
        left-=1
        right+=1

    print(f'{left} {right}',end='')
    print()

