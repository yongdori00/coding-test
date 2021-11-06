from itertools import combinations

def solution(orders, course):
    answer = []

    array = []
    combinations_list = []

    for i in range(len(orders)):
        for j in range(len(orders[i])):
            if orders[i][j] not in array:
                array.append(orders[i][j])

    for i in range(len(course)):
        temp_str = list(combinations(array, course[i]))
        combinations_list.append(temp_str)


    return answer

if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))