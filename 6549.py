# # import sys,math
# # input= sys.stdin.readline


# # def dac(li,start,end):
# #     if end==start:
# #         return li[end]
# #     elif end - start ==1:
# #         if li[end] < li[start]:
# #             return max(2*li[end], li[start])
# #         else:
# #             return max(2*li[start],li[end])
        
    
# #     mid = (start+end)//2

# #     left_area= dac(li,start,mid)
# #     right_area= dac(li,mid+1,end)

# #     left= mid-1
# #     right= mid+1

# #     mid_area=li[mid]
# #     cur_height=li[mid]

# #     while start<=left and right<= end:
# #         if li[left] < li[right]:
# #             if li[right] < cur_height:
# #                 cur_height=li[right]
# #             mid_area=max(mid_area, cur_height *(right-left))
# #             right+=1

# #         else:
# #             if li[left] < cur_height:
# #                 cur_height=li[left]
# #             mid_area = max(mid_area, cur_height * (right-left))
# #             left-=1
    
# #     while start<=left:
# #         if li[left] < cur_height:
# #             cur_height=li[left]
# #         mid_area = max(mid_area, cur_height *(right-left))
# #         left-=1
    
# #     while right<=end:
# #         if li[right]< cur_height:
# #             cur_height = li[right]
# #         mid_area = max(mid_area, cur_height *(right-left))
# #         right+=1

# #     return max(left_area,right_area,mid_area)



# # res=[]
# # while True:
# #     li= list(map(int,input().split()))

# #     if li[0]==0:
# #         break

# #     N=li[0]
# #     sq=li[1:]

# #     res.append(dac(li,0,N-1))

# # for val in res:
# #     print(val)




# import sys
# input = sys.stdin.readline

# def largest_rectangle(heights):
#     n = len(heights)
#     left = [-1] * n  # left[i]: 왼쪽에서 heights[i]보다 작은 첫 번째 위치
#     right = [n] * n  # right[i]: 오른쪽에서 heights[i]보다 작은 첫 번째 위치
    
#     # left 배열 계산 (왼쪽에서 오른쪽으로)
#     stack = []
#     for i in range(n):
#         # 현재 높이보다 높거나 같은 막대들을 스택에서 제거
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         left[i] = stack[-1] if stack else -1
#         stack.append(i)
    
#     # right 배열 계산 (오른쪽에서 왼쪽으로)
#     stack = []
#     for i in range(n-1, -1, -1):
#         # 현재 높이보다 높거나 같은 막대들을 스택에서 제거
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         right[i] = stack[-1] if stack else n
#         stack.append(i)
    
#     # 각 막대를 높이로 하는 최대 직사각형의 넓이 계산
#     max_area = 0
#     for i in range(n):
#         area = heights[i] * (right[i] - left[i] - 1)
#         max_area = max(max_area, area)
#     return max_area

# res = []
# while True:
#     li = list(map(int, input().split()))
    
#     if li[0] == 0:
#         break
    
#     N = li[0]
#     heights = li[1:]
    
#     res.append(largest_rectangle(heights))

# for val in res:
#     print(val)

import sys
input = sys.stdin.readline

def largest_rectangle_dc(heights, left, right):
    # 구간이 비어있음
    if left > right:
        return 0
    
    # 구간에 막대가 하나만 있음
    if left == right:
        return heights[left]
    
    mid = (left + right) // 2
    
    # 1. 왼쪽 구간의 최대 직사각형 
    left_max = largest_rectangle_dc(heights, left, mid)
    
    # 2. 오른쪽 구간의 최대 직사각형 
    right_max = largest_rectangle_dc(heights, mid + 1, right)
    
    # 3. 중간 지점을 포함하는 최대 직사각형
    # mid를 포함해서 양쪽으로 확장하면서 최대 넓이 구하기
    cross_max = 0
    min_height = heights[mid]
    
    # mid에서 시작하는 직사각형
    cross_max = max(cross_max, min_height)
    
    # 양쪽으로 확장
    i, j = mid - 1, mid + 1
    
    while i >= left or j <= right:
        # 왼쪽과 오른쪽 중 더 높은 쪽으로 확장
        if i >= left and (j > right or heights[i] >= heights[j]):
            min_height = min(min_height, heights[i])
            width = j - i
            cross_max = max(cross_max, min_height * width)
            i -= 1
        else:
            min_height = min(min_height, heights[j])
            width = j - i
            cross_max = max(cross_max, min_height * width)
            j += 1
    
    # 세 경우 중 최댓값 반환
    return max(left_max, right_max, cross_max)

def largest_rectangle(heights):
    n = len(heights)
    if n == 0:
        return 0
    return largest_rectangle_dc(heights, 0, n - 1)

res = []
while True:
    li = list(map(int, input().split()))
    
    if li[0] == 0:
        break
    
    N = li[0]
    heights = li[1:]
    
    res.append(largest_rectangle(heights))

for val in res:
    print(val)