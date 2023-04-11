def solution(numbers):
    answer = [0]* len(numbers)
    stack = []

# 타임 아웃
#     for i in range(len(numbers) - 1, -1, -1):
#         if not behind or max(behind) <= numbers[i]:
#             answer.append(-1)
#             behind.append(numbers[i])
#         else:
#             index = len(behind) - 1
#             while behind[index] <= numbers[i]:
#                 index -= 1
            
#             behind.append(numbers[i])
#             answer.append(behind[index])
            
#         print(behind)
    
#     answer.reverse()

    for i in range(0, len(numbers)):
        #이번 인덱스의 수가 스택에 저장된 인덱스의 수보다 크다면 큰 수 저장
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        # Stack에 큰 수를 찾지 못한 숫자들 저장
        stack.append(i)
        
    # 큰 수를 찾지 못한 모든 수들
    while stack:
        answer[stack.pop()] = -1
    
    return answer