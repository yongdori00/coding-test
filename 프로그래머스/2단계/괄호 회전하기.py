from collections import deque

def solution(s):
    answer = 0

    sPer_deque = deque(s)
    stack = []

    #길이가 1~1000이라서 그냥 매번 회전 때마다 deque를 뒤에 붙이고, 해당 deque로 stack으로 괄호 새로 테스트 해줘도 됨. O(n^2) 성립 -> 1,000,000까지는 되나봄.
    for j in range(len(s)):
        stack = []
        for i in sPer_deque:
            if not stack:
                stack.append(i)
                continue
            if i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            answer += 1

        sPer_deque.append(sPer_deque.popleft())


    #효율성에 문제가 생길까봐 회전시키면서 바로 stack, deque가 성립하는지 체크하는 방법을 했으나 헛수고
    # for i in s:
    #     if not stack:
    #         stack.append(i)
    #         continue
    #     if i == "]" and stack[-1] == "[":
    #         stack.pop()
    #     elif i == "}" and stack[-1] == "{":
    #         stack.pop()
    #     elif i == ")" and stack[-1] == "(":
    #         stack.pop()
    #     else:
    #         stack.append(i)

    # if not stack:
    #     answer += 1

    # for i in s[:-1]:
    #     print(stack)
        
    #     if stack:
    #         if i == "]" and stack[-1] == "[":
    #             stack.pop()
    #         elif i == "}" and stack[-1] == "{":
    #             stack.pop()
    #         elif i == ")" and stack[-1] == "(":
    #             stack.pop()
    #         else:
    #             stack.append(i)
    #     else:
    #         stack.append(i)

    #     if not stack:
    #         answer += 1

    return answer

print(solution("}]()[{"))