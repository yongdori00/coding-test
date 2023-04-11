from itertools import permutations

def solution(numbers):
    answer = 0

    lists = []
    primelist = []

    for i in range(1, len(numbers)+1):
        lists.append(list(permutations(numbers, i)))
        for j in range(len(lists[i - 1])):
            lists[i - 1][j] = ''.join(lists[i - 1][j])

    lists = list(map(int, sum(lists, [])))
    lists = list(set(lists))

    for i in range(len(lists)):
        if lists[i] == 0 or lists[i] == 1:
            continue

        if lists[i] == 2 or lists[i] == 3:
            answer += 1
            continue
        
        j = 2
        while j * j < lists[i]:
            if lists[i] % j == 0:
                break
            if (j + 1) * (j + 1) > lists[i]:
                answer += 1
            j += 1


    return answer

print(solution("011"))