n = int(input())
answer = 1
cnt = 0

while n > 0:
    answer *= n
    while (answer % 10) == 0:
        cnt += 1
        answer //= 10
    n -= 1

print(cnt)