def solution(sizes):
    answer = 0

    height = 0
    width = 0

    for i in sizes:
        if i[0] > i[1]:
            tempheight = i[0]
            tempwidth = i[1]
        else:
            tempheight = i[1]
            tempwidth = i[0]

        if tempheight > height:
            height = tempheight
        if tempwidth > width:
            width = tempwidth
        
    answer = height * width

    return answer

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))