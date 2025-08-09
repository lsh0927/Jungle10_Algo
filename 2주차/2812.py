import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = input().rstrip()

stack = []
remove_count = 0

for digit in number:
    while stack and stack[-1] < digit and remove_count < K:
        stack.pop()
        remove_count += 1
    
    stack.append(digit)

while remove_count < K:
    stack.pop()
    remove_count += 1

print(''.join(stack))