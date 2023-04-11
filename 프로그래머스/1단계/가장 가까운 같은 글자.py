def solution(s):
    answer = []
    
    #알파벳마다 가장 마지막에 나온 인덱스를 dict로 저장
    alpha_dict = {}
    
    for i in range(len(s)):
        #한번도 안나온 알파벳 위치 -1로 초기화
        if alpha_dict.get(s[i], -1) == -1:
            answer.append(-1)
        else:
        #가장 가까운 알파벳과의 거리 차이 추가
            answer.append(i - alpha_dict[s[i]])
        #현재 인덱스로 알파벳 dict 업데이트
        alpha_dict[s[i]] = i
    
    return answer