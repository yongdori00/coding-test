def solution(t, p):
    answer = 0
    
    p_int = int(p)
    
    #부분 문자열을 int로 바꿔서 비교
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= p_int:
            answer += 1
    
    return answer