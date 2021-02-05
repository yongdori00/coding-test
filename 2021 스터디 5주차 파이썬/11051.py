num1, num2 = map(int, input().split())

answer = 1

print(num2)

for i in range(num2, 0, -1):
    answer *= num1
    num1 -= 1

        answer //= i
    answer %= 10007

print(answer)