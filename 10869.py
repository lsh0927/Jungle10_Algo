import sys
a,b= map(int,sys.stdin.readline().split())


print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)



# map
# int 
# split


# "1 2 3".split() -> ['1','2','3']
# "1,2,3".split(',') -> , 제거하고 리스트
# "apple-banana".split('-') -> ['apple','banana']
# input().split() -> 공백기준 분리

# int(값) 혹은 int(값, 진법)
# int("123")     # 123
# int("456")     # 456
# int(3.14)      # 3 (소수점 버림)
# int("1010", 2) # 10 (2진법으로 해석)




# # 리스트의 각 원소에 적용하려면 반복문 필요
# numbers = ["1", "2", "3"]
# result = []
# for num in numbers:
#     result.append(int(num))

# map(함수, 반복 가능 객체)
# 기본 사용법
# map(int, ["1", "2", "3"])  # map 객체 반환
# list(map(int, ["1", "2", "3"]))  # [1, 2, 3]

# 언패킹으로 변수에 할당
# a, b = map(int, ["10", "20"])  # a=10, b=20
# a, b, c = map(int, ["1", "2", "3"])  # a=1, b=2, c=3