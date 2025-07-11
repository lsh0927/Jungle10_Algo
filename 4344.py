import sys,math
input= sys.stdin.readline

C= int(input())

def get_avg(scores):
    # sum=0
    # for i in range(0,len(scores)):
    #     sum+=scores[i]
    
    # return sum/len(scores)
    return sum(scores) / len(scores)



for _ in range(C):
    # 하나는 정수로, 나머지는 list로 받을 수 있는 방법
    a= list(map(int, input().split()))
    # N=score[0]
    # score=score.pop(0)
    N = a[0]
    scores = a[1:]  

    length=len(scores)
    cnt=0
    avg=get_avg(scores)
    
    for i in range(length):
        if scores[i]>avg:
            cnt+=1
    #부동소수점 정밀도 문제
    # print(f'{round(cnt/length,3)*100}%')
    print(f'{round(cnt/length*100,3)}%')