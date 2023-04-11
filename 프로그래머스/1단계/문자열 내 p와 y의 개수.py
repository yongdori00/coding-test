def solution(s):
    answer = True
    numP = 0
    numY = 0

    s = s.lower()

    for i in range(len(s)):
        if s[i] == 'p':
            numP += 1
        elif s[i] == 'y':
            numY += 1

    if numP != numY:
        answer = False

    return answer

print(solution("ypyP"))