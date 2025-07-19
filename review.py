import sys
input = sys.stdin.readline

N = int(input())


# def nsum(n):
#     if n==0:
#         return 0

#     return n+ nsum(n-1)

# print(nsum(N))


# tail recursion : 중간 값을 알 수가 있음(추적)
# 언어마다 지향하는 방식이 다름: 반복문이 있으면 비추, 왜??
# def sum(n,total):
#     if n==0:
#         return total
    
#     return sum(n-1,total+n)


# print(sum(N,0))

# def fast_exp(n,b):
#     if n==0:
#         return 1
    
#     if n%2==0:
#         return fast_exp(n/2,b) * fast_exp(n/2,b)
#     else:
#         return b * fast_exp(n-1,b)

#counting change problem

# K=4
# li=[1,2,3] -> 가능한 경우는 4가지

# 1: 주어진 금액 4에 대해 첫째 동전 1을 제외하고 거슬러줄수 있는 경우의 수 : [2,3] ->coins[i]
# 2: 1을 포함해서 푸는 경우

def c(amount,coins):
    if amount==0:
        return 1
    if amount <0 or len(coins)==0:
        return 0
    
    return c(amount,coins[1:]) + c(amount-coins[0],coins)