from collections import deque

def solution(food):
    answer = '0'

    answer_list = deque(answer)

    #가운데로 갈 수록 큰 값이므로 큰 값들을 0기준으로 좌우로 먼저 붙이는 방법으로 하면 됨.
    for i in range(len(food) - 1, 0, -1):
        while food[i] - 2 >= 0:
            answer_list.append(str(i))
            answer_list.appendleft(str(i))
            food[i] -= 2

    answer = ''.join(answer_list)

    return answer