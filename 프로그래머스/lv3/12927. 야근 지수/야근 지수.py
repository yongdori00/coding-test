import math

def solution(n, works):
    answer = 0
    
    works.sort(reverse=True)
    cur_index = 0
    next_index = 0
    
    while n > 0:
        while next_index + 1 < len(works) and works[next_index] <= works[next_index + 1]:
            next_index += 1
        if works[next_index] == 0:
            return 0
        if n >= (next_index + 1):
            n -= (next_index + 1)
            works[next_index] -= 1
        else:
            break
    
    answer += n * int(math.pow((works[next_index] - 1), 2))
    answer += (next_index - n + 1) * int(math.pow(works[next_index], 2))
    
    while (next_index + 1) < len(works):
        answer += int(math.pow(works[next_index + 1], 2))
        next_index += 1
    
    return answer