def solution(number, k):
    stack = []
    removed = 0
    
    for num in number:
        # 스택의 top이 현재 숫자보다 작으면 제거
        while stack and stack[-1] < num and removed < k:
            stack.pop()
            removed += 1
        stack.append(num)
    
    # 만약 k개에 못 미친다면 뒤에서 제거
    for i in range(k-removed):
        stack.pop()
    
    return ''.join(stack)


