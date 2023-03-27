def solution(operations):
    answer = []

    split_oper = []

    cnt = 0

    #deque랑 heapq가지고 헛짓거리 했었음.
    for i in operations:
        split_oper.append(i.split())

    for i in split_oper:
        if i[0] == "I":
            num = int(i[1])
            answer.append(num)
            answer.sort()
            cnt += 1
        elif i[0] == "D":
            if cnt == 0:
                continue
            if i[1] == "1":
                answer.pop()
            elif i[1] == "-1":
                answer.pop(0)
            cnt -= 1

    if cnt == 0:
        answer = [0,0]
    else:
        answer = [answer[-1], answer[0]]

    return answer