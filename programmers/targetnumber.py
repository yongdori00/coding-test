def dfs(numbers, index, minus, target, cur, answer):
    cur = cur + numbers[index] * minus
    
    if index + 1 == len(numbers):
        if target == cur:
            return answer + 1
        else:
            return answer
    else:
        answer = dfs(numbers, index + 1, 1, target, cur, answer)
        answer = dfs(numbers, index + 1, -1, target, cur, answer)
    
    return answer

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, 1, target, 0, answer)
    answer = dfs(numbers, 0, -1, target, 0, answer)
    return answer

print(solution([1, 1, 1, 1, 1], 3))