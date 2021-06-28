def solution(n):
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

print(solution(30))    