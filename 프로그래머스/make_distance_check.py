def solution(places):
    answer = []
    places_list = []
    row_list = []
    col_list = []
    perfectlybreak = False
    nearP = 0

    for i in range(5):
        for j in range(5):
            for k in range(5):
                col_list.append(places[i][j][k])
            row_list.append(col_list)
            col_list = []
        places_list.append(row_list)
        row_list = []
    
    for i in range(5):
        answer.append(1)
        print(i)
        for j in range(5):
            for k in range(5):
                if (places_list[i][j][k] == 'P'):
                    tempj = j - 1
                    tempk = k
                    if ((tempj >= 0) and (places_list[i][tempj][tempk] == 'P')):
                        answer[i] = 0
                        perfectlybreak = True
                        break
                    tempj = j + 1
                    tempk = k
                    if ((tempj < 5) and (places_list[i][tempj][tempk] == 'P')):
                        answer[i] = 0
                        perfectlybreak = True
                        break
                    tempj = j
                    tempk = k - 1
                    if ((tempk >= 0) and (places_list[i][tempj][tempk] == 'P')):
                        answer[i] = 0
                        perfectlybreak = True
                        break
                    tempj = j
                    tempk = k + 1
                    if ((tempk < 5) and (places_list[i][tempj][tempk] == 'P')):
                        answer[i] = 0
                        perfectlybreak = True
                        break
                elif (places_list[i][j][k] == 'O'):
                    nearP = 0
                    tempj = j - 1
                    tempk = k
                    if ((tempj >= 0) and (places_list[i][tempj][tempk] == 'P')):
                        nearP = nearP + 1

                    tempj = j + 1
                    tempk = k
                    if ((tempj < 5) and (places_list[i][tempj][tempk] == 'P')):
                        nearP = nearP + 1

                    tempj = j
                    tempk = k - 1
                    if ((tempk >= 0) and (places_list[i][tempj][tempk] == 'P')):
                        nearP = nearP + 1

                    tempj = j
                    tempk = k + 1
                    if ((tempk < 5) and (places_list[i][tempj][tempk] =='P')):
                        nearP = nearP + 1

                    if (nearP >= 2):
                        answer[i] = 0
                        perfectlybreak = True
                        break
                else:
                    continue
            if perfectlybreak == True:
                perfectlybreak = False
                break
    
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])