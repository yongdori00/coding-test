def solution(num):
    answer = 0
    count = 0

    while count < 500:
        if num == 1:
            answer = count
            break
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        count += 1

    if count == 500:
        answer = -1
    return answer

print(solution(1))