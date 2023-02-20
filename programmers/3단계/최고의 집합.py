def solution(n, s):
    
    if s // n == 0:
        return [-1]
    
    #요소간에 최대한 차이가 적은 경우가 곱했을 때 최대값이 된다.
    #s // n한 값들로 먼저 채운다.
    answer = [s // n] * n
    
    #오름차순이니까 뒷자리 부터 나머지들을 하나씩만 더해준다.
    for i in range(len(answer) - 1, len(answer) - 1 - s % n, -1):
        answer[i] += 1
    
    return answer