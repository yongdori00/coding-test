import numpy as np

def solution(numbers, hand):
    answer = ''
    answer_list = []
    left_status = 0
    right_status = 0
    left_distance = 0
    right_distance = 0
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer_list = list(answer)
            answer_list.append('L')
            answer = ''.join(answer_list)
            left_status = i
        elif i == 3 or i == 6 or i == 9:
            answer_list = list(answer)
            answer_list.append('R')
            answer = ''.join(answer_list)
            right_status = i
        else:
            if i == 0:
                if right_status % 3 != 0:
                    left_distance = np.sqrt(np.exp((left_status / 3) + 1 - ((11 / 3) + 1)) + np.exp((left_status % 3) - (11 % 3)))
                    right_distance = np.sqrt(np.exp((right_status / 3) + 1 - ((11 / 3) + 1)) + np.exp((right_status % 3) - (11 % 3)))
                else:
                    left_distance = np.sqrt(np.exp((left_status / 3) + 1 - ((11 / 3) + 1)) + np.exp((left_status % 3) - (11 % 3)))
                    right_distance = np.sqrt(np.exp((right_status / 3) - ((11 / 3) + 1)) + np.exp(3 - (11 % 3)))

            else:
                if right_status % 3 != 0:
                    left_distance = np.sqrt(np.exp((left_status / 3) + 1 - ((i / 3) + 1)) + np.exp((left_status % 3) - (i % 3)))
                    right_distance = np.sqrt(np.exp((right_status / 3) + 1 - ((i / 3) + 1)) + np.exp((right_status % 3) - (i % 3)))
                else:
                    left_distance = np.sqrt(np.exp((left_status / 3) + 1 - ((i / 3) + 1)) + np.exp((left_status % 3) - (i % 3)))
                    right_distance = np.sqrt(np.exp((right_status / 3) - ((i / 3) + 1)) + np.exp(3 - (i % 3)))
                
            if (left_distance < right_distance)  or ((right_distance == left_distance) and (hand == 'left')):
                answer_list = list(answer)
                answer_list.append('L')
                answer = ''.join(answer_list)
                left_status = i
            elif (right_distance < left_distance) or ((right_distance == left_distance) and (hand == 'right')):
                answer_list = list(answer)
                answer_list.append('R')
                answer = ''.join(answer_list)
                right_status = i

        print(left_status, right_status)
        print(left_distance, right_distance)

    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")