answer = []

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    num_list = list(input())
    list_set = []

    rotate = N // 4
    for j in range(rotate):
        for i in range(4):
            index = i * rotate
            one_rotate = []
            for k in range(rotate):
                one_rotate.append(num_list[(index + k - j) % N])
            #문자열의 진법을 10진법으로 바꿔주는게 내장되어있다.
            list_set.append(int(''.join(one_rotate), 16))

    list_set = set(list_set)
    list_set = list(list_set)

    list_set.sort(reverse=True)
    answer.append(list_set[K - 1])

for i in range(len(answer)):
    print('#' + str(i + 1) + ' ' + str(answer[i]))