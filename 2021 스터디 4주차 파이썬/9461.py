n = int(input())

for i in range (n):
    answer = 0
    size = int(input())

    arr = [0 for i in range(size)]

    if size <= 3:
        for i in range(size):
            arr[i] = 1
        answer = arr[size - 1]
        print(answer)
        continue
    elif size > 3:
        for i in range(3):
            arr[i] = 1

    if 3 < size & size <= 5:
        for i in range(3, size):
            arr[i] = 2
        answer = arr[size - 1]
        print(answer)
        continue
    elif size > 5:
        for i in range(3, 5):
            arr[i] = 2

    for i in range(5, size):
        arr[i] = arr[i - 5] + arr[i - 1]

    answer = arr[size - 1]
    print(answer)
