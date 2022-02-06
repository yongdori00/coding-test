import re

def solution(files):
    answer = []
    HNT = []
    head = re.compile('[a-zA-Z. -]+')
    number = re.compile('[0-9]+')
    tail = re.compile('[A-Za-z0-9. -]+')

    for i in files:
        headA = ''
        numA = ''
        tailA = ''
        headA = head.findall(i)[0]
        i = i.lstrip(headA)
        numA = number.findall(i)[0]
        i = i.lstrip(numA)
        #lstip이 아니라 replace로 하였더니 "f12.12"라는 문자열에서 12가 모두 사라져 버리는 일이 생겨버림
        if i != '':
            tailA = tail.findall(i)[0]
            #빈 문자열이 아닐 때임.

        temp = [headA, numA, tailA]

        for j in range(len(HNT)):
            if HNT[j][0].lower() > temp[0].lower() or ((HNT[j][0].lower() == temp[0].lower()) and (int(HNT[j][1]) > int(temp[1]))):
                HNT.insert(j, temp)
                break
                #뒤의 경우 보다 앞에 놓여야 하는 경우
            elif len(HNT) - 1 == j:
                HNT.append(temp)
                #insert로는 마지막까지 도달 했을 때를 해결 못함.

        if len(HNT) == 0:
            HNT.append(temp)
            #길이 0일 때의 경우
    
    for i in range(len(HNT)):
        answer.append(''.join(HNT[i]))

    return answer

solution(["F12.1", "f012", "FF012"])