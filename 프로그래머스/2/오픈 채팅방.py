def solution(record):
    answer = []
    strlist = ['님이 들어왔습니다.', '님이 나갔습니다.']
    dic_uid_name = {}

    for string in record:
        list_ = string.split()
        if list_[0] == 'Enter' or list_[0] == 'Change':
            dic_uid_name[list_[1]] = list_[2]

    for string in record:
        list_ = string.split()
        if list_[0] == 'Enter':
            name = dic_uid_name.get(list_[1])
            number = 0
            answer.append(name + strlist[number])
        elif list_[0] == 'Leave':
            name = dic_uid_name.get(list_[1])
            number = 1
            answer.append(name + strlist[number])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


def solution(record):
    answer = []
    recordList = []
    preResultList = []
    uidDict = {}

    #레코드 내부의 문자열을 공백 단위로 쪼갬
    for i in range(len(record)):
        recordList.append(record[i].split())

    #엔터, 리브, 체인지에 따라 uid + 님이 XXX했습니다. 를 만들고 uid dictionary에 정보를 저장, 갱신함.
    for i in range(len(record)):
        if recordList[i][0] == 'Enter':
            preResultList.append([recordList[i][1], '님이 들어왔습니다.'])
            uidDict[recordList[i][1]] = recordList[i][2]
        elif recordList[i][0] == 'Leave':
            preResultList.append([recordList[i][1], '님이 나갔습니다.'])
        elif recordList[i][0] == 'Change':
            uidDict[recordList[i][1]] = recordList[i][2]

    for i in range(len(preResultList)):
        preResultList[i][0] = uidDict[preResultList[i][0]]
        answer.append(''.join(preResultList[i]))

    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))