def solution(participant, completion):
    answer = ''

#마라톤 출발 한 사람 n 도착한 사람 n-1인데 그 중 도착하지 못한 사람 찾는건데 동명이인이 있을 수 있음
#아래 주석처리한 코드처럼 participant를 for loop을 써 not in을 쓰려 했는데 중복의 경우가 있는 경우 안되어서

#    for i in participant:
#        if i not in completion:
#            answer = i

#정렬을 한 후 같은 인덱스인데 다른 요소가 있는 첫번째 요소의 participant의 요소 값을 답으로 썼다.

    participant.sort()
    completion.sort()

    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        if i == (len(participant) - 2):
            answer = participant[i + 1]
        
    return answer