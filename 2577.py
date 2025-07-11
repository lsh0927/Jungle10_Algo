import sys,math
input= sys.stdin.readline

from collections import Counter


# A= int(input())
# B= int(input())
# C= int(input())

# val= A*B*C

# digits= str(val)
# # print(list)

# #result=[]
# result = [0] * 10

# for char in digits:
#     #배열의 인덱스에 해당하는 원소의 개수을 대입
#     # 자바라면
#     # arr[Integer.parseInt(digits.charAt(i))-1]+=1
#     result[int(char)]+=1

# for count in result:
#     print(count)



A = int(input())
B = int(input()) 
C = int(input())

counter = Counter(str(A * B * C))
for i in range(10):
    print(counter[str(i)])



# # 수동으로 세기 (현재 코드 방식)
# digits = "1223"
# count = [0] * 10
# for char in digits:
#     count[int(char)] += 1
# # count[1]=1, count[2]=2, count[3]=1

# # Counter로 세기 -> 기본 내림차순
# from collections import Counter
# digits = "1223"
# counter = Counter(digits)
# print(counter)  # Counter({'2': 2, '1': 1, '3': 1})