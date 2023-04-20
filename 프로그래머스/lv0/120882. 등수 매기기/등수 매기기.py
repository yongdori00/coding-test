def solution(score):
    answer = []
    
    order_list = []
    cur = 0
    num = 0
    order = 0
    
    #인덱스, 합산 값
    for i in range(len(score)):
        order_list.append([i, score[i][0] + score[i][1]])
    
    #합산 값으로 내림차순
    order_list.sort(reverse = True, key = lambda x : x[1])
    
    for i in range(len(order_list)):
        #저장된 값이랑 현재가 같으면 등수 그대로
        if cur == order_list[i][1]:
            order_list[i].append(order)
        #작아지면 현재 i값을 등수로
        else:
            order_list[i].append(i+1)
            cur = order_list[i][1]
            order = i+1
    
    #인덱스 기준으로 오름차순
    order_list.sort(key = lambda x : x[0])
    
    #등수만 순서대로 뽑기
    for i in order_list:
        answer.append(i[2])
    
    return answer