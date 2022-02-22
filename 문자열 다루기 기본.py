import re

def solution(s):
    answer = True

    condition = re.compile('[a-zA-Z]')

    if len(s) != 4 and len(s) != 6:
        answer = False    
    if condition.search(s):
        answer = False

    return answer

print(solution('1234'))