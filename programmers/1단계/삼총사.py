from itertools import combinations

def solution(number):
    answer = 0
    
    #3개의 조합
    com_list = list(combinations(number, 3))
    
    #각 조합의 합 중 합이 0인 것 카운트
    for i in com_list:
        if sum(i) == 0:
            answer += 1
    
    return answer