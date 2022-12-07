def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] is False:
            absolutes[i] *= -1
        answer += absolutes[i]

    return answer