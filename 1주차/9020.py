import sys, math
input = sys.stdin.readline

T = int(input())

isPrime = [True] * 10001
isPrime[0] = False
isPrime[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(10001)) + 1):
    if isPrime[i]:
        for j in range(i*i, 10001, i):  
            isPrime[j] = False

for _ in range(T):
    n = int(input())
    left = n // 2
    right = n // 2
    
    # 둘 다 소수가 될 때까지 반복
    while not (isPrime[left] and isPrime[right]):
        left -= 1
        right += 1
    
    print(left, right)