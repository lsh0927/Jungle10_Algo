import sys,math
input= sys.stdin.readline

T= int(input())

for _ in range(T):
    line= input().split()
    n= int(line[0])
    str= line[1]

    #str의 각 원소를 n번 더한 걸 출력
    res=''
    for i in range(len(str)):
        for _ in range(n):
            res+=str[i]
    print(res)