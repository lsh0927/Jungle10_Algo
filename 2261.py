import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
   li.append(tuple(map(int, input().split())))

# X값 기준 정렬
li.sort()

def cal_mid(mid,start,end,min_dist):
    # 가운데 영역 고려
    check_point = []
    divide_x = li[mid][0]
    for i in range(start, end + 1):  # end 포함
       if (li[i][0] - divide_x)**2 <= min_dist:
           check_point.append(li[i])
    
    check_point.sort(key=lambda x: x[1])

    for i in range(len(check_point)):
       now = check_point[i]
       for j in range(i+1, len(check_point)):
           compare = check_point[j]
           # y 좌표를 기준으로 현재 기준점에서의 거리가 min이상이면 가지치기 
           if (compare[1] - now[1])**2 >= min_dist:
               break
           dist = (now[0] - compare[0])**2 + (now[1] - compare[1])**2
           min_dist = min(min_dist, dist)
    
    return min_dist
    

def get_min(start, end):  # end는 inclusive
    if start == end:  # 원소 1개
        return 1000000000
    if end - start == 1:  # 원소 2개
        return (li[start][0] - li[end][0])**2 + (li[start][1] - li[end][1])**2
   
    # 분할정복
    mid = (start + end) // 2
    left = get_min(start, mid)
    right = get_min(mid + 1, end)
    min_dist = min(left, right)

    min_dist= cal_mid(mid,start,end,min_dist)
    return min_dist
   


print(get_min(0, N-1))