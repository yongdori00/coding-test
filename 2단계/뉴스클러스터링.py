def solution(str1, str2):
    answer = 0

    str1 = str1.upper()
    str2 = str2.upper()

    str1ele = []
    str2ele = []

    union = {}

    for i in range(len(str1ele) - 1):
        str1ele.append(tuple(str1[i:i+1]))
    
    for i in range(len(str2ele) - 1):
        str2ele.append(tuple(str2[i:i+1]))

    for i in str1ele:
        union[i] = union.get(i, 0) + 1
    for i in str2ele:
        union[i] = union.get(i, 0) + 1

    intersection = [key for key, value in union.items() if value > 1]
    
    unilen = len(union)
    intlen = len(intersection)

    answer = intlen/unilen

    return answer