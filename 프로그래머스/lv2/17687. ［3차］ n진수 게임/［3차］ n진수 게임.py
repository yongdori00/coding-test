from collections import deque

def solution(n, t, m, p):
    answer = []
    
    radix = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    re_list = ['0']
    
    total_num = t * m
    cur_num = 0
    temp_p = p - 1
    
    for i in range(total_num):
        #차례라면 그 숫자를 저장
        if i % m == temp_p:
            answer.append(re_list.pop())
        else:
            re_list.pop()
            
        if not re_list:
            cur_num += 1
            temp_cur_num = cur_num
            while temp_cur_num > 0:
                mod = temp_cur_num % n
                temp_cur_num //= n
                re_list.append(radix[mod])
    
    return ''.join(answer)