def solution(n, m):
    answer = []

    if n < m:
        temp = n
        n = m
        m = temp

    tempn = n
    tempm = m

    while tempn % tempm != 0:
        temp = tempn % tempm
        tempn = tempm
        tempm = temp
    
    answer.append(tempm)
    answer.append(n*m/tempm)

    return answer