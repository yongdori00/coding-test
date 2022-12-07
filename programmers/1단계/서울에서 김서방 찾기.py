def solution(seoul):
    index = 0

    index = seoul.index('Kim')
    
    answer = '김서방은 ' + str(index) + '에 있다'

    return answer

print(solution(["Jane", "Kim"]))