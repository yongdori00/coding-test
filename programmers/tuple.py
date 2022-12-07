def solution(s):
    answer = []

    list_an = s.split("},{")

    first = list_an[0][2:]
    list_an[0] = first
    last = list_an[-1][:-2]
    list_an[-1] = last


    list_an.sort(key = len)
    
    for i in range(len(list_an)):
        list_an[i] = list_an[i].split(',')
        for j in range(len(list_an[i])):
            list_an[i][j] = int(list_an[i][j])
    

    for i in range(len(list_an)):
        pivot = list_an[i][0]
        answer.append(list_an[i][0])
        for j in range(i, len(list_an)):
            list_an[j].remove(pivot)

    return answer

print(solution("{{123}}"))