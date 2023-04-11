'''from itertools import combinations

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
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))'''

from itertools import combinations

def solution(orders, course):
    answer = []
    orderslist = []
    coursecomb = {}
    
    for i in orders:
        orderslist.append(list(i))
    
    for j in orderslist:
        for i in course:
            k = list(combinations(j,i))
            for m in k:
                coursecomb[m] = coursecomb.get(m, 0) + 1

    answer.append(list(key for key, value in coursecomb.items() if value > 1))
    
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))