def solution(x, n):
    answer = []

    if x == 0:
        answer = [0 for i in range(n)]
    #x가 0인 경우에는 for range에서 에러남
    else:
        for i in range(x, x*(n+1), x):
            answer.append(i)

    return answer

print(solution(0, 3))