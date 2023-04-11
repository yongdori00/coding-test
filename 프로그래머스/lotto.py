def solution(lottos, win_nums):
    answer = []
    most = 0
    least = 0
    
    for i in lottos:
        if i in win_nums:
            most += 1
            least +=1
            win_nums.remove(i)
            print(i)

    for i in lottos:
        if i == 0:
            most += 1
    
    if most >= 2:
        answer.append(7 - most)
    else:
        answer.append(6)
    if least >= 2:
        answer.append(7 - least)
    else:
        answer.append(6)

    return answer

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))