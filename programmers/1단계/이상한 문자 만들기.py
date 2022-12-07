def solution(s):
    answer = []
    s = list(s)
    count = 0

    for i in range(len(s)):
        if s[i].isalpha():
            if count % 2 == 0:
                s[i] = s[i].upper()
            elif count % 2 != 0:
                s[i] = s[i].lower()
            count += 1

        #소문자->대문자 뿐만 아니라 대문자->소문자도 해줘야함.
        else:
            count = 0
            
    answer = ''.join(s)
    print(s)
    return answer

print(solution("aA ba bab cacc c cca "))