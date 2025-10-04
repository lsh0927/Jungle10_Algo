def solution(arr):
    ans=[]
    for val in arr:
        if not ans:
            ans.append(val)
        else:
            if ans[-1]==val:
                continue
            else:
                ans.append(val)
            
    return ans