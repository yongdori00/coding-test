def solution(msg):
    answer = []
    w = [msg[0]]

    alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for i in range(len(msg)):
        # print(alp)
        #현재의 문자열을 임시로 복사
        temp_w = w[:]
        #마지막 전까지는 이어 붙이기
        if i < len(msg) - 1:
            c = msg[i + 1]
            temp_w.append(c)
        # print(msg[i])
        # print(temp_w)
        #alp에 지금 문자열이 없으면 추가하기
        if ''.join(temp_w) not in alp:
            append_word = ''.join(temp_w)
            alp.append(append_word)
            answer.append(alp.index(''.join(w)) + 1)
            # print(append_word)
            w = [msg[i + 1]]
        else:
            if i != len(msg) - 1:
                w = temp_w[:]
            if i == len(msg) - 1:
                answer.append(alp.index(''.join(w)) + 1)

        # print()
    return answer
