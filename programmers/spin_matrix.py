def solution(rows, columns, queries):
    answer = []
    array = []

    for i in range(rows):
        temp_array = []
        for j in range(1, columns+1):
            temp_array.append(i*columns + j)
        array.append(temp_array)
    
    for i in range(len(queries)):
        min_num = 10001
        x = queries[i][1] - 1
        y = queries[i][0] - 1
        temp1 = array[y][x]
        temp2 = 0

        while (x < queries[i][3] - 1):
            if min_num > temp1:
                min_num = temp1
            temp2 = array[y][x + 1]
            array[y][x + 1] = temp1
            temp1 = temp2
            x = x + 1

        while (y < queries[i][2] - 1):
            if min_num > temp1:
                min_num = temp1
            temp2 = array[y + 1][x]
            array[y + 1][x] = temp1
            temp1 = temp2
            y = y + 1

        while(x > queries[i][1] - 1):
            if min_num > temp1:
                min_num = temp1
            temp2 = array[y][x - 1]
            array[y][x - 1] = temp1
            temp1 = temp2
            x = x - 1

        while(y > queries[i][0] - 1):
            if min_num > temp1:
                min_num = temp1
            temp2 = array[y - 1][x]
            array[y - 1][x] = temp1
            temp1 = temp2
            y = y - 1
            

        answer.append(min_num)

    return answer

if __name__ == '__main__':
    print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))