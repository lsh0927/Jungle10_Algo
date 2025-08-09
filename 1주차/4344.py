import sys,math
input= sys.stdin.readline

C= int(input())

def get_avg(scores):
    return sum(scores) / len(scores)

for _ in range(C):
    # 하나는 정수로, 나머지는 list로 받을 수 있는 방법
    a= list(map(int, input().split()))
    N = a[0]
    scores = a[1:]  

    length=len(scores)
    cnt=0
    avg=get_avg(scores)
    
    for i in range(length):
        if scores[i]>avg:
            cnt+=1

    print(f'{round(cnt/length*100,3)}%')