def solution(s):
    
    stack=[]
    for ch in s:
        if not stack:
            if ch==')':
                return False
            else:
                stack.append(ch)
        else:
            if stack[-1]=='(' and ch==')':
                stack.pop()
            else: 
                stack.append(ch)                
            
    if stack:
        return False
    else:
        return True