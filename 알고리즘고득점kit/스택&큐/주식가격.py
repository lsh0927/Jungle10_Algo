def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        # prices[i]의 가격을 tmp에 저장
        tmp= prices[i]
        for j in range(i+1,len(prices)):
            # 끝까지 가격이 떨어지지 않은 경우의 기간
            time=len(prices)-i-1
            
            # 만약 이후의 가격이 prices[i] 보다 작다면 기간은 그때를 기준으로업데이트
            if prices[j]<prices[i]:
                time=j-i
                break
            
        answer.append(time)
        
            
    answer[-1]=0
    return answer