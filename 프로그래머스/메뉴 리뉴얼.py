'''from itertools import combinations 

def solution(orders, course):
    answer = []
    alphabet = []
    alphabetCom = []
    num = 0
    
    for i in orders:
        for j in i:
            if j not in alphabet:
                alphabet.append(j)
    alphabet.sort()

    for i in course:
        alphabetCom += list(combinations(alphabet, i))

    for tuples in alphabetCom:
        num = 0
        for string in orders:
            include = True
            for alp in tuples:
                if alp not in string:
                    print(alp)
                    include = False
                    break
            if include is True:
                num += 1
            if num >= 2:
                answer.append(''.join(tuples))
                break

    answer.sort()

    return answer'''
    
def solution(orders, course):
    answer = []
    alphabet = []
    alphabetCom = []
    num = 0
    
    for i in orders:
        for j in i:
            if j not in alphabet:
                alphabet.append(j)
    alphabet.sort()

    return answer