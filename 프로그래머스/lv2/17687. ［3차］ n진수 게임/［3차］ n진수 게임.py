#나눠서 나온 값의 인덱스에서 구하려 했는데 stack으로 풀어도 되는걸 중간에 깨닳음.

from collections import deque

def solution(n, t, m, p):
    answer = []
    
    radix = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    re_list = ['0']
    
    total_num = t * m
    cur_num = 0
    temp_p = p - 1
    
    #인원 수(m) * 구해야하는 숫자의 갯수(바퀴 수)(t)를 해서 순환은 돌아야함.
    for i in range(total_num):
        #차례라면 그 숫자를 저장
        if i % m == temp_p:
            answer.append(re_list.pop())
        #아니라면 그냥 pop
        else:
            re_list.pop()
            
        #이번 숫자를 진법으로 변환 후 스택으로 넣는다.
        #이유: 4는 2진법으로 100이라는 숫자이며 만약 2로 계속 나눈 나머지를 순서대로 넣으면 오히려 [0,0,1]이 될 것임.
        #이후에는 1, 0, 0이라는 순서로 부를 것이기 때문에 stack으로 생각하고 append, pop을 사용하면 됨.
        if not re_list:
            cur_num += 1
            temp_cur_num = cur_num
            #n진법의 나머지들 append
            while temp_cur_num > 0:
                mod = temp_cur_num % n
                temp_cur_num //= n
                re_list.append(radix[mod])
    
    return ''.join(answer)