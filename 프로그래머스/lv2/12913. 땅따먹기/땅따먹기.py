def solution(land):
    answer = 0

    #["제일 큰 값의 인덱스", "제일 큰 값의 합", "두번째로 큰 값의 인덱스", "두번째로 큰 값의 합"]
    max_list = [[0 for i in range(4)] for i in range(len(land))]

    #일단 index = 0 일때를 초기화 해줌.
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
            #합이 제일 큰 길의 인덱스와 다른 경우(max_list[i - 1][0]과 j의 비교 )
            if max_list[i - 1][0] != j:
                #새로 더해서 구한 값이 기존 값보다 큰 경우 제일 큰 값으로 바꿔줌
                if max_list[i][1] < max_list[i - 1][1] + land[i][j]:
                    max_list[i][3] = max_list[i][1]
                    max_list[i][2] = max_list[i][0]
                    max_list[i][1] = max_list[i - 1][1] + land[i][j]
                    max_list[i][0] = j
                #두번째로 큰 값보다 큰 경우 바꿔줌.
                elif max_list[i][3] < max_list[i - 1][1] + land[i][j]:
                    max_list[i][3] = max_list[i - 1][1] + land[i][j]
                    max_list[i][2] = j
            #합이 제일 큰 길의 인덱스와 같아서 강제로 합이 두번쨰로 큰 길의 인덱스와 더해야하는 경우(max_list[i - 1][2]와 j의 비교)
            else:
                if max_list[i][1] < max_list[i - 1][3] + land[i][j]:
                    max_list[i][3] = max_list[i][1]
                    max_list[i][2] = max_list[i][0]
                    max_list[i][1] = max_list[i - 1][3] + land[i][j]
                    max_list[i][0] = j
                elif max_list[i][3] < max_list[i - 1][3] + land[i][j]:
                    max_list[i][3] = max_list[i - 1][3] + land[i][j]
                    max_list[i][2] = j
    
    #마지막 인덱스에서 최대값
    answer = max_list[len(max_list) - 1][1]
    
    return answer