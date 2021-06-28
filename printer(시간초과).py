MIN = -1

def solution(priorities, location):
    answer = 0

    cycle = 0
    pivot = len(priorities) - 1
    maxnum_index = 0
    current_index = pivot

    while cycle < len(priorities):
        current_index = pivot + 1
        while current_index != pivot:
            if current_index == len(priorities):
                current_index = 0

            if priorities[current_index] > priorities[maxnum_index]:
                maxnum_index = current_index

            current_index += 1

        pivot = maxnum_index
        cycle += 1
        priorities[pivot] = MIN
                
        if maxnum_index == location:
            answer = cycle
            break

    return answer

print(solution([2,1,3,2], 0))