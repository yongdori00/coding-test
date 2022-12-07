def is_index_zero(priorities, index):
    if index == 0:
        index = len(priorities) - 1
    else:
        index -= 1
    return index

def solution(priorities, location):
    answer = 0
    pivot = 0
    index = location

    while True:
        if priorities[0] < max(priorities[0:]):
            priorities.append(priorities.pop(0))
            index = is_index_zero(priorities, index)
        else:
            priorities.pop(0)
            answer += 1
            if index == 0:
                break
            index = is_index_zero(priorities, index)

    return answer

print(solution([1, 1, 9, 1, 1, 1],0))