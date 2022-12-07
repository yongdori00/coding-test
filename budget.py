def solution(d, budget):
    answer = 0
    cur = 0
    i = 0
    d.sort()
    while i < len(d) and (cur + d[i] <= budget):
        cur += d[i]
        answer += 1
        i += 1
    return answer