def solution(num):
    answer = 0

#2로 나누어지면 2로 나누고 그렇지 않으면 3을 곱한 뒤 1을 더하는 코드임
#500번 시도할 경우에도 안되면 -1을 하라고 하는데 효율성 따지지 않고 모든 케이스 하면됨.

    if num != 1:
        while answer < 500:
            if num % 2 == 0:
                num = num // 2
            elif num % 2 == 1:
                num = num * 3 + 1

            answer = answer + 1

            if num == 1:
                break
        if answer == 500:
            answer = -1

    return answer

print(solution(626331))