def solution(relation):
    answer = 0

    head = 0
    pivot = 0
    tail = 0

    translist = []

    for i in range(len(relation[0])):
        temp = []
        for j in range(len(relation)):
            temp.append(relation[j][i])
        translist.append(temp)

    for i in range(len(translist)):
        if len(set(translist[i])) == len(translist[i]):
            length = len(translist[i])
            for j in range(length):
                relation[j].pop(i)
                answer+=1

    print(relation)

    '''for i in range(len(translist)):
        head = i
        for j in range()
        tail+=
        tempcat = []
        translist
'''

    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])