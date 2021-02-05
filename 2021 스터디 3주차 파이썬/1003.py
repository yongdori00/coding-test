def fibonacci_(gotN, answer_list):
    if gotN == 0:
        answer_list[0] += 1
        return 0
    elif gotN == 1:
        answer_list[1] += 1
        return 1
    else:
        return fibonacci_((gotN - 1), answer_list) + fibonacci_((gotN - 2), answer_list)

n = int(input())
answer_list = [0, 0]
num_list = []

for i in range(0, n):
    num_list.append(int(input()))

for i in range(0, n):
    fibonacci_(num_list[i], answer_list)
    print(str(answer_list[0]) + ' ' + str(answer_list[1]))
    answer_list[0] = 0
    answer_list[1] = 0

