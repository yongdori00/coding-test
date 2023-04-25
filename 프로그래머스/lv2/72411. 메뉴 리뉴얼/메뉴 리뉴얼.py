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
    
    for i in range(len(orders)):
        if max_ < len(orders[i]):
            max_ = len(orders[i])
            
    while course[-1] > max_:
        course.pop()
            
    for j in orders:
        for i in course:
            if len(j) >= i:
                comb_list += list(combinations(list(j), i))
    
    comb_str_list = []
    
    for i in comb_list:
        comb_str_list.append(''.join(sorted(i)))
    
    for i in comb_str_list:
        dict_[i] = dict_.get(i, 0) + 1
        
    list_ = list()
    for key, value in dict_.items():
        list_.append((key, value))
    
    list_.sort(key = lambda x : len(x[0]))
    
    index = 0
    max_len = 0
    max_str_course_index = []
    max_str_index = []
    
    for i in list_:
        if course[index] == len(i[0]):
            if i[1] > max_len and i[1] > 1:
                max_len = i[1]
                max_str_index = [i[0]]
            elif i[1] == max_len and i[1] > 1:
                max_str_index.append(i[0])
                
        elif course[index] < len(i[0]):
            max_str_course_index += list(max_str_index)
            index += 1
            max_len = 0
            if i[1] >= max_len and i[1] > 1:
                max_len = i[1]
                max_str_index = [i[0]]
    
    max_str_course_index += list(max_str_index)
    set_ = set(max_str_course_index)
    answer = sorted(set_)
    
    return answer