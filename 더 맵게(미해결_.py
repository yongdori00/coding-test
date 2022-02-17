def solution(scoville, K):
    answer = 0

    while scoville[0] < K:
        scoville.append(scoville.pop(0) + scoville.pop(0) * 2)
        
        index = len(scoville) - 1
        while index > 0 and scoville[index] < scoville[(index - 1) // 2]:
            temp = scoville[index]
            scoville[index] = scoville[(index - 1) // 2]
            scoville[(index - 2) // 2] = temp

        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12]	, 7))