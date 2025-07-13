#요소 값들의 분산이 최소일 때 값이 최소로 나옴.(큰 수를 먼저 줄여서 평균을 맞추는게 중요)
#heapsort로 풀어보려 했으나 시간 초과남.

import math

def solution(n, works):
    answer = 0
    
    #일단 정렬 해야함.
    works.sort(reverse=True)
    cur_index = 0
    next_index = 0
    
    while n > 0:
        #works의 -1 위치까지 이면서 현재 index의 works가 다음보다 큰 위치에 있는 순간까지 next_index 증가
        while next_index + 1 < len(works) and works[next_index] <= works[next_index + 1]:
            next_index += 1
        #만약 마지막 index의 값이 0이면 0출력 (모든 인덱스가 0이라는 얘기)
        if works[next_index] == 0:
            return 0
        #만약 현재의 index까지의 갯수보다 빼야할 수가 더 남았다면 
        #0 ~ index까지 -1을 한다고 가정해서 works[next_index]에만 -1을 해줌.
        #이게 중요함. 전체를 빼는 것이 아닌 경계 위치의 값이 무엇인지.
        if n >= (next_index + 1):
            n -= (next_index + 1)
            works[next_index] -= 1
        #남은 n의 갯수가 index만큼보다 적으면 break
        else:
            break
    
    #남은 n개 만큼은 0 ~ index까지의 숫자들 보다 1씩 작으므로 아래 연산 수행
    answer += n * int(math.pow((works[next_index] - 1), 2))
    #남은 n ~ index 값들 아래 연산 수행
    answer += (next_index - n + 1) * int(math.pow(works[next_index], 2))
    
    #이후 남은 수들 연산 수행
    while (next_index + 1) < len(works):
        answer += int(math.pow(works[next_index + 1], 2))
        next_index += 1
    
    return answer