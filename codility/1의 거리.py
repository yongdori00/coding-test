# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    n = ""
    index = []
    max = 0

    while N > 0:
        if N % 2 == 1:
            n = "1" + n
        else:
            n = "0" + n
        N //= 2

    for i in range(len(n)):
        if n[i] == "1":
            index.append(i)

    for i in range(len(index) - 1):
        temp = 0
        if index[i] < index[i + 1]:
            temp = index[i+1] - index[i]
        else:
            temp = index[i] - index[i+1]

        if temp == 1:
            continue
        else:
            temp -= 1

        if max < temp:
            max = temp

    return max

print(solution(15))