from itertools import permutations

def solution(k, dungeons):
    answer = -1

    permulist = list(permutations(range(len(dungeons)), len(dungeons)))
    #여기 순열로 이용해서 모든 인덱스 조합을 찾아주는 것이 포인트

    for per in permulist:
        tempk = k
        tempanswer = 0
        for i in per:
            if tempk >= dungeons[i][0]:
                tempk -= dungeons[i][1]
                tempanswer += 1
            if tempanswer > answer:
                answer = tempanswer

    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))
