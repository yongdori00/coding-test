first_zero = 1
first_one = 0
second_zero = 0
second_one = 1

num = int(input())
num_list = []
answer_zero = 0
answer_one = 0

for i in range(num):
    num_list.append(int(input()))

for i in range(num):
    if num_list[i] == 0:
        print(str(first_zero) + ' ' + str(first_one))
        continue
    elif num_list[i] == 1:
        print(str(second_zero) + ' ' + str(second_one))
        continue

    for i in range(num_list[i] - 1):
        answer_one = second_one + first_one
        first_one = second_one
        second_one = answer_one

        answer_zero = first_zero + second_zero
        first_zero = second_zero
        second_zero = answer_zero

    print(str(answer_zero) + ' ' + str(answer_one))

    first_zero = 1
    first_one = 0
    second_zero = 0
    second_one = 1