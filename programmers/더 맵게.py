import heapq

def solution(scoville, K):
    answer = 0
    i = 0
    length = len(scoville)

    heapq.heapify(scoville)

    minimum = heapq.heappop(scoville)

    while minimum < K:
        if len(scoville) == 0:
            answer = -1
            return answer
        minimum2 = heapq.heappop(scoville)
        new = minimum + minimum2 * 2
        heapq.heappush(scoville, new)
        minimum = heapq.heappop(scoville)
        answer+=1

    return answer

print(solution([1, 2, 3, 9, 10, 12],104))