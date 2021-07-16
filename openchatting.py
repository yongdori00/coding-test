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