def solution(score):
    answer = []
    
    order_list = []
    cur = 0
    num = 0
    order = 0
    
    for i in range(len(score)):
        order_list.append([i, score[i][0] + score[i][1]])
        
    order_list.sort(reverse = True, key = lambda x : x[1])
    
    for i in range(len(order_list)):
        if cur == order_list[i][1]:
            order_list[i].append(order)
        else:
            order_list[i].append(i+1)
            cur = order_list[i][1]
            order = i+1
    
    order_list.sort(key = lambda x : x[0])
    
    for i in order_list:
        answer.append(i[2])
    
    return answer