def solution(land):
    answer = 0

    #["제일 큰 값의 인덱스", "제일 큰 값", "두번째로 큰 값의 인덱스", "두번째로 큰 값"]
    max_list = [[0 for i in range(4)] for i in range(len(land))]

    for i in range(4):
        if max_list[0][1] < land[0][i]:
            max_list[0][3] = max_list[0][1]
            max_list[0][2] = max_list[0][0]
            max_list[0][1] = land[0][i]
            max_list[0][0] = i
        elif max_list[0][3] < land[0][i]:
            max_list[0][3] = land[0][i]
            max_list[0][2] = i
    
    for i in range(1, len(land)):
        for j in range(4):
            if max_list[i - 1][0] != j:
                if max_list[i][1] < max_list[i - 1][1] + land[i][j]:
                    max_list[i][3] = max_list[i][1]
                    max_list[i][2] = max_list[i][0]
                    max_list[i][1] = max_list[i - 1][1] + land[i][j]
                    max_list[i][0] = j
                elif max_list[i][3] < max_list[i - 1][1] + land[i][j]:
                    max_list[i][3] = max_list[i - 1][1] + land[i][j]
                    max_list[i][2] = j
            else:                
                if max_list[i][1] < max_list[i - 1][3] + land[i][j]:
                    max_list[i][3] = max_list[i][1]
                    max_list[i][2] = max_list[i][0]
                    max_list[i][1] = max_list[i - 1][3] + land[i][j]
                    max_list[i][0] = j
                elif max_list[i][3] < max_list[i - 1][3] + land[i][j]:
                    max_list[i][3] = max_list[i - 1][3] + land[i][j]
                    max_list[i][2] = j
    
    answer = max_list[len(max_list) - 1][1]
    
    return answer