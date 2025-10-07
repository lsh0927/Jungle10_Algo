import heapq as hq

def solution(jobs):
    
    jobs.sort()
    q=[]
    cur_time=0
    total_time=0
    idx=0
    fin=0
    
    while fin<len(jobs):
        while idx<len(jobs) and jobs[idx][0]<=cur_time:
            hq.heappush(q,[jobs[idx][1],jobs[idx][0]])
            idx+=1
        
        if q:
            dur_time,req_time= hq.heappop(q)
            cur_time += dur_time
            total_time+=cur_time-req_time
            fin+=1
        else:
            cur_time = jobs[idx][0]
            
            
    return total_time // len(jobs)
