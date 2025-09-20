import sys
input= sys.stdin.readline

expression = input().strip()
parts = expression.split('-')
result = float('inf')

#print(parts)

for part in parts:
    tmp = 0
    numbers = part.split('+')
    for number in numbers:
        tmp += int(number)
    
    if result == float('inf'):
        result = tmp
    else:
        result -= tmp

print(result)