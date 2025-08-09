import sys,math
input = sys.stdin.readline
# 그냥 input을 사용하는 것보다 개행처리 안한 readline을 쓴 후 후처리를 해주는 것이 훨씬 빠름


# N= int(input())
# li=[]
# for _ in range(N):
#     val= input()
#     if val not in li:
#         li.append(val)
# li.sort(key=lambda x: (len(x),x))


N = int(input())
li = set()

for _ in range(N):
    li.add(input().rstrip())  # readline은 개행 문자 포함

sorted_li = sorted(li, key=lambda x: (len(x), x))
for val in sorted_li:
    print(val)


# C 레벨에서 최적화된 set -> list 변환 구현

# set의 내부 해시 테이블을 순회하면서
# 새로운 리스트 객체에 직접 포인터 복사
# 실제 데이터 복사가 아닌 객체 참조 복사

# set → list 변환
# O(n): 해시 테이블의 각 요소를 한 번씩만 방문

# vs 리스트 중복 제거
# O(n²): 각 요소마다 전체 리스트 검색