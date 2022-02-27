def solution(x):
    answer = True

    xlist = list(map(int, str(int(x))))

    sumA = sum(xlist)

    answer = True if x % sumA == 0 else False

    return answer