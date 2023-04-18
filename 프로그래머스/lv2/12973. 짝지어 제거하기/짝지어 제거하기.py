def solution(s):
    answer = -1
    stack_list = []
    
    for i in range(len(s)):
        if stack_list and stack_list[-1] == s[i]:
            stack_list.pop()
        else:
            stack_list.append(s[i])

    if stack_list:
        return 0
    else:
        return 1