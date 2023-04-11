def solution(numbers):
    answer = ''

    list_ex = [str(i) for i in range(1001)]
    list_num = [0 for i in range(1001)]

    for i in range(len(numbers)):
        list_num[numbers[i]] += 1               #0~1000의 카운팅 정렬을 이용한 후

    list_ex.sort(reverse = True)

    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    for i in range(len(list_ex) - 1):
        if list_ex[i][0] == list_ex[i+1][0]:        #0~1000에 대한 정렬만 하여
            j = 0
            k = i + 1
            while (k < len(list_ex)) and (list_ex[i][j] == list_ex[k][j]):
            #for k in range(i + 1, len(numbers)):
                if int(list_ex[i]+list_ex[k]) < int(list_ex[k]+list_ex[i]):
                    temp = list_ex[i]
                    list_ex[i] = list_ex[k]
                    list_ex[k] = temp
                k += 1

    for i in range(len(list_ex)):
        while list_num[int(list_ex[i])] > 0:       #큰 숫자가 나오면 카운팅 정렬된 값을 하나씩 줄이면서 정렬
            answer = answer + list_ex[i]
            list_num[int(list_ex[i])] -= 1

    '''if len(numbers) == 1:
        answer = str(numbers[0])

    else:
        for i in range(len(numbers)):
            numbers[i] = str(numbers[i])            #여기는 문자열 덧셈으로 비교 했는데 시간 초과 남

        numbers.sort(reverse = True)
        print(numbers)
        
        for i in range(len(numbers) - 1):
            if numbers[i][0] == numbers[i+1][0]:
                j = 0
                k = i + 1
                while (k < len(numbers)) and (numbers[i][j] == numbers[k][j]):
                #for k in range(i + 1, len(numbers)):
                    if int(numbers[i]+numbers[k]) < int(numbers[k]+numbers[i]):
                        temp = numbers[i]
                        numbers[i] = numbers[k]
                        numbers[k] = temp
                    k += 1

                    while j < max(len(numbers[i]), len(numbers[k])):
                        if numbers[i][left] < numbers[k][right]:
                            break
                        elif numbers[i][left] > numbers[k][right]:
                            break
                        j += 1
                        if j > len(numbers[i]) - 1:
                            left = len(numbers[i]) - 1
                        else:
                            left += 1
                            
                        if j > len(numbers[k]) - 1:
                            right = len(numbers[k]) - 1
                        else:
                            right += 1'''
    
    if int(answer) == 0:
        answer = '0'
    return answer

print(solution([0,0,0,0]))