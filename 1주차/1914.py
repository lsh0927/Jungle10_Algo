import sys,math
input= sys.stdin.readline

N= int(input())

def recur(n,start,end,mid):

    if n==1:
        # 1개 남으면 바로 옮김
        print(start,end)
        return 1

    # 1단계 -> n-1개의 원반을 mid로 이동
    cnt1= recur(n-1,start,mid,end)

    # 2단계 -> 젤 큰 원반을 end로 이동
    print(start,end)

    # 3단계
    cnt2= recur(n-1,mid,end,start)

    return cnt1+cnt2+1

total= int(2**N)-1
print(total)

if N<=20:   
    recur(N,1,3,2)