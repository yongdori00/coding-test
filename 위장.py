def solution(clothes):
    answer = 0

    newdict = {}
    newlist = []
    size = 1

    for i in clothes:
        if newdict.get(i[1]) == None:
            newdict[i[1]] = 1
        else:
            newdict[i[1]] += 1

    for key in newdict:
        size *= (newdict[key] + 1)

    answer = size - 1

    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))