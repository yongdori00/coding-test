def solution(elements):
    answer = 0
    #겹치는 숫자는 없게 하기위해서
    ans_set = set()
    
    #순환을 돌 요소의 갯수
    for i in range(1, len(elements) + 1):
        sum_list = elements[:i]
        #한바퀴 도는 순환
        for j in range(len(elements)):
            ans_set.add(sum(sum_list))
            sum_list.pop(0)
            sum_list.append(elements[(j + i) % len(elements)])
            
    ans_list = list(ans_set)         
    answer = len(ans_list)
    return answer