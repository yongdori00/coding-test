def solution(word):
    answer = len(word)

    #읽은 길이를 먼저 저장해줘야함.

    string = 'AEIOU'
    arr = [5 * (5 * (5 * (5 + 1) + 1) + 1) + 1,5 * (5 * (5 + 1) + 1) + 1, 5 * (5 + 1) + 1,5 + 1,1]

    #맨 끝자리는 1개씩
    #끝에서 두번째는 맨 끝이 빈 것 한개를 포함해서 5 + 1
    # ...해서 Xn = 5 * Xn-1 + 1 라는 점화식을 이용한다.

    for i in range(len(word)):
        index = string.find(word[i])
        answer += (arr[i] * index)

    return answer

print(solution("AAAAE"))