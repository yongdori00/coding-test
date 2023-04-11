import operator

def solution(bridge_length, weight, truck_weights):
    answer = 1

    arr = [bridge_length for i in range(len(truck_weights))]
    #onearr = [1 for i in range(len(truck_weights))]

    first_index = 0
    last_index = 0
    current_truck = 0

    while first_index < len(truck_weights):
        if last_index == 0:
            current_truck += truck_weights[last_index]
            last_index += 1
        elif (last_index < len(truck_weights)) and (weight >= current_truck + truck_weights[last_index]):
            current_truck += truck_weights[last_index]
            last_index += 1

        answer += 1

        
        for i in range(first_index, last_index):            #밑의 주석 처리 부분과 아예 같은 기능(시간도 별 차이 안남)
            arr[i] -= 1
        
        #arr[first_index: last_index] = map(operator.sub, arr[first_index: last_index], onearr[first_index: last_index])
        
        if arr[first_index] == 0:
            current_truck -= truck_weights[first_index]
            first_index += 1
        
    return answer

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))