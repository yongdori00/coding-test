d = [0] * 30001

X = int(input())

for i in range(2, X + 1):
    #최소한 i - 1번째보다 +1이기 때문
    d[i] = d[i - 1] + 1

    #각각 나누어 떨어지면 나누어 떨어지는 횟수와 현재 횟수와 최솟값을 비교
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[X])