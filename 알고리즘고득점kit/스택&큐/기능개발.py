def solution(progresses, speeds):
    answer = []
    days = [] 
    
    for i in range(len(speeds)):
        cur_pro = progresses[i]
        tmp = 0
        while cur_pro < 100:
            cur_pro += speeds[i]
            tmp += 1
        days.append(tmp)
        
    count=1
    max_day=days[0]
    
    for i in range(1, len(days)):
        if max_day>= days[i]:
            count+=1
        else:
            answer.append(count)
            count=1
            max_day=days[i]
    
    answer.append(count)
    
    return answer