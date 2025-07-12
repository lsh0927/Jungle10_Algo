import sys,math
from collections import Counter
input= sys.stdin.readline


A= int(input())
B= int(input())
C= int(input())
res = Counter(str(A * B * C))
for i in range(10):
    print(res[str(i)])
