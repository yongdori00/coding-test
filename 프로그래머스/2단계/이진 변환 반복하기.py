def solution(s):
    answer = []
    cnt = 0
    len_cnt = 0
    
    #1이 될 때까지
    while s != "1":
        new_s = []
        length1 = len(s)

        #0을 삭제한 문자열의 길이
        length2 = len(''.join(s.split("0")))
        
        cnt += 1
        #0을 삭제한 갯수의 합
        len_cnt = len_cnt + length1 - length2
        
        #이진 변환 과정
        while length2 != 0:
            new_s.append(str(length2 % 2))
            length2 //= 2
            
        new_s.reverse()
        s = ''.join(new_s)
    
    answer.append(cnt)
    answer.append(len_cnt)
    return answer

print(solution("110010101001"))