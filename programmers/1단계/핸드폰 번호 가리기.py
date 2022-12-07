def solution(phone_number):
    answer = ''
    listphone = list(str(phone_number))

    length = len(listphone)

    for i in range(length - 4):
        listphone[i] = '*'

    answer = ''.join(listphone)

    return answer