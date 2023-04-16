def solution(want, number, discount):
    answer = 0
    dict_fruit = {}
    zero_list = [0 for i in range(len(want))]
    
    for i in range(len(want)):
        dict_fruit[want[i]] = number[i]
        
    #일단 첫 열흘에 대한 연산
    for i in range(10):
        if discount[i] in list(dict_fruit.keys()):
            dict_fruit[discount[i]] -= 1
        
    #number원소의 합은 10이므로 철저하게 zero_list와 같아야함.
    if list(dict_fruit.values()) == zero_list:
        answer += 1
    if len(discount) == 10:
        return answer
        
    #한칸씩 이동하면서 과일 추가, 삭제
    for i in range(len(discount) - 10):
        if discount[i] in list(dict_fruit.keys()):
            dict_fruit[discount[i]] += 1
        if discount[i + 10] in list(dict_fruit.keys()):
            dict_fruit[discount[i + 10]] -= 1
        if list(dict_fruit.values()) == zero_list:
            answer += 1
    
    return answer