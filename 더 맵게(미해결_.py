def solution(scoville, K):
    answer = 0

    scoville.sort()

    while scoville[0] < K:
        scoville[1] = scoville[0] + scoville[1] * 2
        scoville[0] = scoville.pop()

        
        index = len(scoville) - 1
        while index > 0 and scoville[index] < scoville[(index - 1) // 2]:
            temp = scoville[index]
            scoville[index] = scoville[(index - 1) // 2]
            scoville[(index - 1) // 2] = temp

        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12]	, 7))