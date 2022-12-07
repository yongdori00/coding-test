def solution(n):
    answer = []

    strN = str(n)
    fowardlistN = list(strN)
    for i in fowardlistN:
        answer.insert(0, int(i))

    return answer