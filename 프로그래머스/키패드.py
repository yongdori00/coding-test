import numpy as np

def solution(numbers, hand):
    answer = ''
    loc_x = [2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    loc_y = [4, 1, 1, 1, 2, 2, 2, 3, 3, 3]

    start_l = [1, 4]
    start_r = [3, 4]

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            start_l[0] = loc_x[numbers[i]]
            start_l[1] = loc_y[numbers[i]]
            answer = answer + 'L'
        elif numbers[i] == 3 or numbers [i] == 6 or numbers[i] == 9:
            start_r[0] = loc_x[numbers[i]]
            start_r[1] = loc_y[numbers[i]]
            answer = answer + 'R'
        else:
            left_len = abs(start_l[0] - loc_x[numbers[i]])+abs(start_l[1] - loc_y[numbers[i]])
            right_len = abs(start_r[0] - loc_x[numbers[i]])+abs(start_r[1] - loc_y[numbers[i]])
            if left_len < right_len or ((left_len == right_len) and (hand == 'left')):
                start_l[0] = loc_x[numbers[i]]
                start_l[1] = loc_y[numbers[i]]
                answer = answer + 'L'
            elif right_len < left_len or ((left_len == right_len) and (hand == 'right')):
                start_r[0] = loc_x[numbers[i]]
                start_r[1] = loc_y[numbers[i]]
                answer = answer + 'R'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))