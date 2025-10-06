import heapq as hq

def solution(scoville, K):
    
    q=[]
    for x in scoville:
        hq.heappush(q,x)
        
    cnt=0
    while q:
        tmp=hq.heappop(q)
        if tmp>=K:
            return cnt
        else:
            hq.heappush(q,tmp)
            if len(q)<2:
                break
            else:
                hq.heappush(q,hq.heappop(q)+hq.heappop(q)*2)
                cnt+=1
            
    return -1