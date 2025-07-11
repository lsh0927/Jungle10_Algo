
# def to_base(num,base):
#     if num==0:
#         return "0"
    
#     digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result=""

#     while num>0:
#         result= digits[num%base] +result
#         num//=base
    
#     return result

# print(to_base(100,3))


# bin
# oct
# hex



# from collections import Counter
# digits = "1223"
# counter = Counter(digits)
# print(counter)  # Counter({'2': 2, '1': 1, '3': 1})


import time

def performance_test():
    # 테스트 문자
    test_char = 'A'
    iterations = 1000000  # 100만 번 반복
    
    print(f"테스트 문자: '{test_char}'")
    print(f"반복 횟수: {iterations:,}회\n")
    
    # 1. ord() 방법
    start_time = time.time()
    for _ in range(iterations):
        result = ord(test_char)
    ord_time = time.time() - start_time
    
    # 2. encode() 방법
    start_time = time.time()
    for _ in range(iterations):
        result = test_char.encode('ascii')[0]
    encode_time = time.time() - start_time
    
    # 3. bytes() 방법
    start_time = time.time()
    for _ in range(iterations):
        result = bytes(test_char, 'ascii')[0]
    bytes_time = time.time() - start_time
    
    # 결과 출력
    print("성능 비교 결과:")
    print(f"ord():     {ord_time:.4f}초")
    print(f"encode():  {encode_time:.4f}초")
    print(f"bytes():   {bytes_time:.4f}초")
    
    print(f"\n상대적 성능 (ord() 기준):")
    print(f"encode()는 ord()보다 {encode_time/ord_time:.1f}배 느림")
    print(f"bytes()는 ord()보다 {bytes_time/ord_time:.1f}배 느림")
    
    # 결과 검증
    print(f"\n결과 검증:")
    print(f"ord():     {ord(test_char)}")
    print(f"encode():  {test_char.encode('ascii')[0]}")
    print(f"bytes():   {bytes(test_char, 'ascii')[0]}")

if __name__ == "__main__":
    performance_test()