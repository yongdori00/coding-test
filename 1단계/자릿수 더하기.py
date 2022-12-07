def solution(n):
    answer = 0
    
    strN = str(n)
    strlistN = list(strN)

    for i in strlistN:
        answer += int(i)

    return answer