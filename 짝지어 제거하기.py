def solution(s):
    answer = -1
    list_s = []
    index = 0
    
    while index < len(s):
        if len(list_s) == 0 or list_s[len(list_s) - 1] != s[index]:
            list_s.append(s[index])
        else:
            list_s.pop()
        index = index + 1

    if len(list_s) == 0:
        answer = 1
    else:
        answer = 0
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    print(answer)

    return answer

solution('baabaa')