import numpy as np

def solution(N, stages):
    MIN = -1
    answer = []
    ratearr = []
    length = len(stages)
    mom = length
    stage = 1
    while stage <= N:
        son = 0
        for i in range (length):
            if stage == stages[i]:
                son += 1
        if son == 0:
            ratearr.append(0.0)                       #와.... 겨우 실패율 0퍼센트인 값에 0을 따로 넣는거 하나만으로 결과가 달라짐 ㅅㅂ
        else:                                         #(ex:n이 4이고 stage가 3,3,3,3이면 4에 가기 전에 mom이 0이 되기 때문에 division by zero가 나옴)
            ratearr.append(son / mom)
        mom -= son
        stage += 1
    
    ratearr = np.array(ratearr)

    i = 0
    while i < N:
        index = int(np.argmax(ratearr))
        answer.append(index + 1)
        ratearr[index] = MIN
        i += 1
    return answer

print(solution(4, [3, 3, 3, 3]))