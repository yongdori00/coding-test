num = [i for i in range(11)]
word = {'S':1, 'D':2, 'T':3}
reward = {'*':2, '#':-1}

def solution(dartResult):
    answerarr = [0 for i in range(3)]
    index = 0
    sett= 0

    while sett < 3:
        if int(dartResult[index]) in num:
            if (int(dartResult[index]) == 1) and (dartResult[index + 1].isdigit()):
                answerarr[sett] = 10
                index += 1
            else:
                answerarr[sett] = int(dartResult[index])
            index += 1
        
        if dartResult[index] in word:
            answerarr[sett] = pow(answerarr[sett], word.get(dartResult[index]))
            index += 1

        if (index < len(dartResult)) and (dartResult[index] in reward) :
            if dartResult[index] == '*':
                if sett == 0:
                    answerarr[0] *= 2
                else:
                    answerarr[sett - 1] *= 2
                    answerarr[sett] *= 2
            if dartResult[index] == '#':
                answerarr[sett] *= (-1)
            index += 1

        sett += 1
    answer = sum(answerarr)
    return answer

#print(solution('1S*2T*3S'))