def solution(s):
    answer = ''
    answerList = sorted(list(map(int, s.split())))
    
    List = [str(answerList[0]), str(answerList[len(answerList) - 1])]
    
    answer = ' '.join(List)
    return answer