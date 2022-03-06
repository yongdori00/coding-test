def solution(s):
    answer = 0
    slist = []
    
    for i in s:
        if len(slist) == 0:
            slist.append(i)
        elif slist[len(slist) - 1] != i:
            slist.append(i)
        else:
            slist.pop()
            
    if len(slist) == 0:
        answer = 1

    return answer