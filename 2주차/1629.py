import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

A,B,C=map(int,input().split())

# (AxB)%C = (A%C) * (B%C) % C

def func(a,n):
  if n == 1:
      return a%C
  else:
      dev = func(a,n//2)
      if n %2 ==0:
          return (dev * dev) % C
      else:
          return (dev  * dev *a) %C
          
print(func(A,B))