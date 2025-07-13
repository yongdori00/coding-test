def solution(s):
    answer = -1
    stack_list = []
    
    for i in range(len(s)):
        #stack 맨 위랑 다음 문자가 같으면 pop
        if stack_list and stack_list[-1] == s[i]:
            stack_list.pop()
        #아니면 append
        else:
            stack_list.append(s[i])

    if stack_list:
        return 0
    else:
        return 1