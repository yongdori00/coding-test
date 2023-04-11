def solution(s):
    answer = len(s)
    length = len(s)
    cnt = 1
    answer_str = ''

    for i in range(1, length//2 + 1):
        temp = s[:i]
        cnt = 1
        for j in range(i, length, i):
            temp1 = s[j:j+i]
            if temp == temp1:
                cnt += 1
            else:
                if cnt == 1:
                    answer_str += temp
                else:
                    answer_str += (str(cnt) + temp)
                    cnt = 1
                temp = str(temp1)
        if cnt == 1:
            answer_str += temp1
        else:
            answer_str += (str(cnt) + temp)
        if len(answer_str) < answer:
            answer = len(answer_str)
        answer_str = ''

    return answer