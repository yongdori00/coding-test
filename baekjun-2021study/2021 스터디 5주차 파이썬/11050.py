num1, num2 = map(int, input().split())

answer = 1

for i in range(num2):
    answer *= num1
    num1 -= 1

for i in range(1, num2 + 1):
    answer //= i

print(answer)