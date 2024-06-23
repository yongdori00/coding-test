def solution(s):
    answer = ''
    # answerList = sorted(list(map(int, s.split())))
    
    # List = [str(answerList[0]), str(answerList[len(answerList) - 1])]
    
    # answer = ' '.join(List)
    
    list_ = []
    
    s = s.split()
    for i in s:
        list_.append(int(i))
        
    list_.sort()
    
    answer = str(list_[0]) + ' ' + str(list_[-1])
    
    return answer