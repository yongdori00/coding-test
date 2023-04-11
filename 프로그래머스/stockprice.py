def solution(prices):
    cnt = 0
    index = 0
    answer = []
    
    for index in range(len(prices)):
        for i in range(index, len(prices)):
            if prices[index] > prices[i]:
                cnt += 1
                break
            cnt += 1
            
        answer.append(cnt)
        cnt = 0
        
    return answer