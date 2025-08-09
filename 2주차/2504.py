

# arr=input()
# stack=[]

# answer=0
# tmp=1

# for i in range(len(arr)):
#     if arr[i] =='(':
#         stack.append(arr[i])
#         tmp *=2
#     elif arr[i] == '[':
#         stack.append(arr[i])
#         tmp *=3
#     elif arr[i] == ")":
#         if not stack or stack[-1] == "[":
#             answer = 0 
#             break
#         if arr[i-1] == "(":
#             answer += tmp
#         stack.pop()
#         tmp //= 2  
#     else:
#         if not stack or stack[-1] == "(":
#             answer=0
#             break
#         if arr[i-1] =='[':
#             answer+=tmp
#         stack.pop()
#         tmp //=3

# if stack:
#     print(0)
# else:
#     print(answer)

# import sys
# input = sys.stdin.readline

# def solve():
#     s = input().strip()
#     stack = []
    
#     for char in s:
#         if char in '([':
#             stack.append(char)
#         else:  # ')' 또는 ']'
#             temp = 0
            
#             # 숫자들을 모두 더함 (가장 안쪽 계산)
#             while stack and isinstance(stack[-1], int):
#                 temp += stack.pop()
            
#             # 대응되는 여는 괄호 확인
#             if not stack:
#                 return 0
            
#             opening = stack.pop()
#             if (char == ')' and opening != '(') or (char == ']' and opening != '['):
#                 return 0
            
#             # 계산: 빈 괄호면 기본값, 아니면 곱셈
#             if temp == 0:
#                 stack.append(2 if char == ')' else 3)
#             else:
#                 stack.append(temp * (2 if char == ')' else 3))
    
#     # 최종 결과: 숫자만 남아있어야 함
#     result = 0
#     for item in stack:
#         if isinstance(item, int):
#             result += item
#         else:
#             return 0
    
#     return result

# print(solve())

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value  # '(', '[', 또는 숫자
        self.children = []

def build_tree(s):
    """괄호 문자열을 트리로 변환"""
    stack = []
    root = Node('root')
    current = root
    
    for char in s:
        if char in '([':
            new_node = Node(char)
            current.children.append(new_node)
            stack.append(current)
            current = new_node
        else:  # ')' 또는 ']'
            if not stack:
                return None
            
            # 괄호 매칭 검사
            expected = '(' if char == ')' else '['
            if current.value != expected:
                return None
            
            current = stack.pop()
    
    return root if not stack else None

def post_order_calc(node):
    """후위 순회로 계산"""
    if not node.children:  # 리프 노드 (빈 괄호)
        return 2 if node.value == '(' else 3 if node.value == '[' else 0
    
    # 자식들을 먼저 계산 (후위 순회의 핵심!)
    total = 0
    for child in node.children:
        total += post_order_calc(child)
    
    # 현재 노드 계산
    if node.value == '(':
        return total * 2
    elif node.value == '[':
        return total * 3
    else:  # root
        return total

def solve():
    s = input().strip()
    
    # 트리 구축
    tree = build_tree(s)
    if tree is None:
        return 0
    
    # 후위 순회로 계산
    return post_order_calc(tree)

print(solve())