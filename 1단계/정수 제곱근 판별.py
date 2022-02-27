import math

def solution(n):
    answer = 0

    sqrt = int(math.sqrt(n))

    if sqrt ** 2 == n:
        answer = (sqrt + 1) ** 2
    else:
        answer = -1

    return answer