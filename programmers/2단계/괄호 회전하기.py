from collections import deque

def solution(s):
    answer = 0

    s_deque = deque(s)

    for i in s:
        print(s_deque)

        pop = ""

        if s_deque:
            pop = s_deque.popleft()
        else:
            pop = i
            s_deque.append(pop)
            continue
        
        if s_deque:
            if pop == "]" and s_deque[-1] == "[":
                s_deque.pop()
            elif pop == "}" and s_deque[-1] == "{":
                s_deque.pop()
            elif pop == ")" and s_deque[-1] == "(":
                s_deque.pop()
        else:
            s_deque.append(pop)

        if not s_deque:
            answer += 1

    return answer

print(solution("}]()[{"))