import sys,math
input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

N= int(input())
li= list(map(int, input().split()))

# 이분 탐색을 통해 search안의 원소가 있는지 확인
M= int(input())
search= list(map(int, input().split()))

midIdx= N//2 


for val in search:
    isContain=0
    left=0
    right=N-1
    
    while left<=right:
        midIdx=(left+right)//2
        if val== li[midIdx]:
            isContain=1
            break
        elif val< li[midIdx]:
            right=midIdx-1            
        else: 
            left=midIdx+1

    print(isContain)

