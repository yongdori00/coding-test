'''def solution(progresses, speeds):
    answer = []
    new_list = []
    index = 0

    numberOfReturn = 1

    for i in range(len(progresses)):
        rest_num = 100 - progresses[i]
        if rest_num % speeds[i] != 0:
            rest_num //= speeds[i]
            rest_num += 1
        else:
            rest_num //= speeds[i]

        new_list.append(rest_num)

    for i in range(len(new_list) - 1):
        if new_list[index] >= new_list[i + 1]:
            numberOfReturn += 1
        else:
            answer.append(numberOfReturn)
            index = i + 1
            numberOfReturn = 1
        if i + 1 == len(new_list) - 1:
            answer.append(numberOfReturn)

    return answer

print(solution([99, 70, 96], [1, 30, 5]))'''

def solution(progresses, speeds):
    completed = []
    answer = []

    completed = []

    for i in range(len(progresses)):
        completed.append((100 - progresses[i]) // speeds[i])
        if (100 - progresses[i]) % speeds[i] != 0:
            completed[i] += 1

    print(completed)

    i = 0
    while i <len(completed):
        temp = 1
        j = i + 1
        while j < len(completed):
            if completed[i] >= completed[j]:
                temp += 1
            else:
                break
            j += 1
        
        answer.append(temp)
        i += temp

    return answer