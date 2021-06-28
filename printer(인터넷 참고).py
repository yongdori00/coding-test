def solution(priorities, location):
    answer = 0

    index_array = [i for i in range(len(priorities))]
    num_array = priorities.copy()

    i = 0

    while True:
        if num_array[i] < max(num_array[i + 1:]):
            index_array.append(index_array.pop(i))
            num_array.append(num_array.pop(i))
        else:
            i += 1
        
        if num_array == sorted(num_array, reverse=True):
            break

    return index_array.index(location) + 1

print(solution([1, 2, 3, 2],3))