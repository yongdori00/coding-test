def solution(n):
    answer = 0
    strN = str(int(n))
    #int 타입으로 한번 더 해줘야함.
    strlist = list(strN)

    answer = sorted(strlist, reverse = True)

    answer = int(''.join(answer))

    return answer

print(solution(8000000000))