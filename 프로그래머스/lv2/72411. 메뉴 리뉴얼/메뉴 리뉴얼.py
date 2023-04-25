from itertools import combinations

def solution(orders, course):
#     answer = []
#     list_orders = []
#     set_orders = set()
#     max_ = 0
    
#     for i in range(len(orders)):
#         if max_ < len(orders[i]):
#             max_ = len(orders[i])
            
#     while course[-1] > max_:
#         course.pop()
            
#     for i in orders:
#         list_orders.append(list(i))
#         for j in i:
#             set_orders.add(j)
            
#     for i in course:
#         comb_list = list(combinations(set_orders, i))
#         result = []
#         max_num = 0
#         for j in comb_list:
#             cur_num = 0
#             s_j = set(j)
#             for k in list_orders:
#                 if s_j.issubset(set(k)):
#                     cur_num += 1
#             if cur_num > max_num:
#                 if cur_num > 1:
#                     result = [j]
#                 max_num = cur_num
#             elif cur_num == max_num and max_num > 1:
#                 result.append(j)
#         answer += result
    
#     new_answer = []
    
#     for i in range(len(answer)):
#         new_answer.append(''.join(sorted(answer[i])))
#     new_answer.sort()

    answer = []
    dict_ = {}
    comb_list = []
    max_ = 0
    
    #orders의 최대 문자열 길이가 course의 값보다 크면 해당 course 값은 pop
    for i in range(len(orders)):
        if max_ < len(orders[i]):
            max_ = len(orders[i])
    
    
    while course[-1] > max_:
        course.pop()
            
    #orders에 대해서 모두 combinations를 수행
    for j in orders:
        for i in course:
            if len(j) >= i:
                comb_list += list(combinations(list(j), i))
    
    comb_str_list = []
    
    #문자 리스트 -> 정렬된 문자열로 변환
    for i in comb_list:
        comb_str_list.append(''.join(sorted(i)))
    
    #key:value를 해서 중복 값은 갯수를 찾아간다.
    for i in comb_str_list:
        dict_[i] = dict_.get(i, 0) + 1
        
    #dict -> list(tuple(key, value))
    list_ = list()
    for key, value in dict_.items():
        list_.append((key, value))
    
    #문자열의 길이로 오름차순 정렬
    list_.sort(key = lambda x : len(x[0]))
    
    index = 0
    max_len = 0
    max_str_course_index = []
    max_str_index = []
    
    #각 문자열 길이 마다 최대 값들 뽑아내기
    for i in list_:
        #기존 문자열 길이인 경우
        if course[index] == len(i[0]):
            #갯수가 최대로 갱신되면 값도 갱신
            if i[1] > max_len and i[1] > 1:
                max_len = i[1]
                max_str_index = [i[0]]
            #갯수가 같으면 append
            elif i[1] == max_len and i[1] > 1:
                max_str_index.append(i[0])
                
        #문자열의 길이가 늘어났을 때
        #기존 최대값 리스트 저장
        #course의 index + 1, 최대값 초기화
        elif course[index] < len(i[0]):
            max_str_course_index += list(max_str_index)
            index += 1
            max_len = 0
            #바로 큰 값이 나타났을 때
            if i[1] >= max_len and i[1] > 1:
                max_len = i[1]
                max_str_index = [i[0]]
    
    #마지막 문자열 일단 연결
    max_str_course_index += list(max_str_index)
    #중복 제거
    set_ = set(max_str_course_index)
    #사전식 정렬, 리스트로 변환
    answer = sorted(set_)
    
    return answer