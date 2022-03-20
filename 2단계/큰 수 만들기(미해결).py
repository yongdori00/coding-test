from itertools import combinations

def solution(number, k):
    answer = ''
    tempanswer = []

    n = len(number)
    m = n - k

    numList = list(number)

    tempk = k
    for i in range(len(numList)):
        if len(tempanswer) == 0:
            tempanswer.append(numList[i])
            tempk -= 1
        
        if tempk

    

print(solution("1231234", 3))