def solution(s):
    answer = ''

    lists = []

    t = ''

    for i in range(len(s)):

        #연속 공백일 경우 continue
        if s[i] == ' ':
            t = t + ' '
            if i < len(s) - 1 and s[i + 1] == ' ':
                continue
        #공백 이전의 문자열, 숫자까지 continue
        elif s[i].isalpha() or s[i].isdigit():
            t = t + s[i]
            if i < len(s) - 1 and s[i + 1].isalpha():
                continue
        lists.append(t)
        t = ''

    for i in lists:
        temp = ''
        for j in range(len(i)):
            tempJ = ''
            #첫번쨰 문자가 알파벳일 경우 대문자로 변경
            if j == 0 and i[j].isalpha():
                tempJ = i[j].upper()
            #첫번째 이외의 문자일 경우 소문자로 변경
            elif i[j].isalpha():
                tempJ = i[j].lower()
            #숫자, 공백은 그대로
            else:
                tempJ = i[j]
            
            temp = temp + tempJ

        answer = answer + temp

    return answer

print(solution("  3id  sfaw3ef  "))