def solution(price, money, count):
    answer = -1
    
    allcount = (1+count) * (count/2)
    totalnum = price * allcount
    
    answer = totalnum - money
    
    if answer <= 0:
        answer = 0
    
    return answer