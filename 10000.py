# import sys,math
# input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

# N=int(input())
# li=[]
# for _ in range(N):
#     li.append(list(map(int, input().split())))


# r의 값을 기준으로 내림차순 정렬?
# 원이 나타내는 영역은?
# 원이 주어지면, x값으로만 겹치는지 아닌지 알 수 있나?
# 맨 바깥쪽 영역이 있기때문에 1이 시작
# 각 원마다, Lidx가 있고 Ridx가 있을 것
# 탐색해나가면서 두 인덱스를 찾음

# [[-9,11], [0,20], [7,5], [11,9]]
# 만약에 x 기준으로 정렬이 된다면, 
# 0번째 원의 Lidx= -9-11 = -20, Ridx= -9+11 = 2
# 1번째 원의 Lidx= 0-20 = -20, Ridx= 0+20 =20
# 2번째 원의 Lidx= 7-5 = 2, Ridx= 7+5 = 12
# 3번째 원의 Lidx= 11-9 = 2, Ridx= 11+9 = 20

# 그럼 Lidx, Ridx를 각각 따로 정렬?
# 스택을 2개 써야하나

import sys
input = sys.stdin.readline

n = int(input())

values = []
for _ in range(n):
    c, r = list(map(int, input().split()))
    values.append(["L", c-r])
    values.append(["R", c+r])
values.sort(key=lambda p: (-p[1], p[0]), reverse=True)

stack = []
count = 1

for value in values:
    if value[0] == "L":
        stack.append(value)
    else:
        cum_width = 0

        while stack:
            prev = stack.pop()

            if prev[0] == "L":
                width = value[1] - prev[1]

                # 너비가 같으면 +2
                if width == cum_width:
                    count += 2
                else:
                    count += 1

                stack.append(["C", width]) 
                break

            # 내부원
            elif prev[0] == "C":
                cum_width += prev[1]
    
print(count)# import sys,math
# input= sys.stdin.readline
# sys.stdin.readline는 개행문자를 포함한채로 비교

# N=int(input())
# li=[]
# for _ in range(N):
#     li.append(list(map(int, input().split())))


# r의 값을 기준으로 내림차순 정렬?
# 원이 나타내는 영역은?
# 원이 주어지면, x값으로만 겹치는지 아닌지 알 수 있나?
# 맨 바깥쪽 영역이 있기때문에 1이 시작
# 각 원마다, Lidx가 있고 Ridx가 있을 것
# 탐색해나가면서 두 인덱스를 찾음

# [[-9,11], [0,20], [7,5], [11,9]]
# 만약에 x 기준으로 정렬이 된다면, 
# 0번째 원의 Lidx= -9-11 = -20, Ridx= -9+11 = 2
# 1번째 원의 Lidx= 0-20 = -20, Ridx= 0+20 =20
# 2번째 원의 Lidx= 7-5 = 2, Ridx= 7+5 = 12
# 3번째 원의 Lidx= 11-9 = 2, Ridx= 11+9 = 20

# 그럼 Lidx, Ridx를 각각 따로 정렬?
# 스택을 2개 써야하나

import sys
input = sys.stdin.readline

n = int(input())

values = []
for _ in range(n):
    c, r = list(map(int, input().split()))
    values.append(["L", c-r])
    values.append(["R", c+r])
values.sort(key=lambda p: (-p[1], p[0]), reverse=True)

stack = []
count = 1

for value in values:
    if value[0] == "L":
        stack.append(value)
    else:
        cum_width = 0

        while stack:
            prev = stack.pop()

            if prev[0] == "L":
                # 두 점간 거리: 0이면 접함
                diff = value[1] - prev[1]

                # 너비가 같으면 +2
                if diff == cum_width:
                    count += 2
                else:
                    count += 1

                stack.append(["C", diff]) 
                break

            # 내부원
            elif prev[0] == "C":
                cum_width += prev[1]
    
print(count)