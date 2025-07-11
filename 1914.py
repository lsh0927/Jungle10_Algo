import sys,math
input= sys.stdin.readline


N= int(input())

F=1
E=2
T=3




def hanoi(N,start,end,mid):
    if N == 1:
    # 원판이 1개일 때는 바로 옮기기
        print(start, end)
        return 1
    
    # n-1개를 start에서 mid로 옮기기
    cnt1 = hanoi(N-1, start, mid, end)

    # 아래 1개를 바로 옮기기
    print(start,end)
    
    # mid에 있는 n-1를 end로 옮기기
    cnt2 = hanoi(N-1, mid, end, start)
    return cnt1+cnt2+1

# 총 이동 횟수는 2^n - 1
total = (2 ** N) - 1
print(total)

# N이 20 이하일 때만 경로 출력
if N <= 20:
    hanoi(N, 1, 3, 2)

# hanoi(1)를 하면 횟수는?
# 1 3
# 1회

# hanoi(2)를 하면 횟수는?
# 1 2
# 1 3
# 2 3
# 3회

# 3회로 늘어났을때 from과 to가 바뀐다면
# 2 1
# 2 3
# 1 3

# hanoi(3)를 하면 횟수는?
# 1 3
# 1 2
# 3 2
# 1 3


# 2 1
# 2 3
# 1 3
# 7회