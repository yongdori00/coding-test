'''def solution(n):
    answer = ''
    
    while n > 0:
        if n % 3 == 0:
            answer += '1'
            n -= 2
        elif n % 3 == 1:
            answer += '2'
            n -= 1
        else:
            answer += '4'
            n -= 3
        n //= 3
    
    return answer

print(solution(30))'''


def solution(n):
    answer = ''

    remainder = 0

    while n > 0:
        remainder = n % 3
        n = n // 3

        if remainder == 0:
            answer = '4' + answer
            n = n - 1
        elif remainder == 1:
            answer = '1' + answer
        elif remainder == 2:
            answer = '2' + answer

    return answer