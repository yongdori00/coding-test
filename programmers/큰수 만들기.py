def solution(number, k):
    answer = ''

    number = list(map(int, number))

    answerList = [0]

    for i in range(len(number)):
        for j in range(len(answerList)):
            if number[i] > answerList[j] and len(number) - i - 1 >= len(number) - k - j - 1:
                del answerList[j:]
                answerList.append(number[i])
                break
            if j == len(answerList) - 1 and len(answerList) < len(number) - k:
                answerList.append(number[i])

    for i in range(len(answerList)):
        answerList[i] = str(answerList[i])
    answer = ''.join(answerList)
    return answer

print(solution("1924",2))