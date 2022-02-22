def solution(strings, n):
    answer = []

    answer = strings

    for i in range(len(answer)):
        for j in range(i, len(answer)):
            if answer[i][n] > answer[j][n]:
                temp = answer[i]
                answer[i] = answer[j]
                answer[j] = temp

            elif answer[i][n] == answer[j][n]:
                if answer[i] > answer[j]:
                    temp = answer[i]
                    answer[i] = answer[j]
                    answer[j] = temp

    return answer

print(solution(["sun", "bed", "car"],1))