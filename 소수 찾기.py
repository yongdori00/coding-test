def solution(n):
    answer = 0
    arrlist = [False for i in range(n + 1)]

    for i in range(2, n + 1):
        #소수가 아니라면 continue
        if arrlist[i]:
            continue

        answer += 1
        #해당 숫자보다 작은 소수가 없으므로 해당 소수의 배수들을 전부 True로 바꿔줌
        for k in range(i, n + 1, i):
            arrlist[k] = True


    return answer