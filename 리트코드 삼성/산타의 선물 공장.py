from collections import deque
import copy

roop_ = int(input())

belt_id = []
belt_weight = []
belt = []
answer = []

for i in range(roop_):
    list_ = list(map(int, input().split()))
    if list_[0] == 100:
        n, m = list_[1], list_[2]
        for j in range(n//m):
            belt_id.append(copy.deepcopy(list_[3 + j * m: 3 + (j + 1) * m]))
        for j in range(n//m, n//m*2):
            belt_weight.append(copy.deepcopy(list_[3 + j * m: 3 + (j + 1) * m]))
        for j in range(len(belt_id)):
            temp = []
            for k in range(len(belt_id[j])):
                temp.append({belt_id[j][k]: belt_weight[j][k]})
            belt.append(temp)
        print(belt)

    elif list_[0] == 200:
        sum = 0
        for i in range(len(belt)):
            first = list(belt[i].values())[0]
            if list_[1] >= first:
                sum += first
                belt[i].pop(0)
        answer.append(sum)

    print(answer)

    # elif list_[0] == 300:
    # elif list_[0] == 400:
    # elif list_[0] == 500: