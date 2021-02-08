n = int(input())
num1, num2 =0, 0

while n != 0:
    answer = 1
    n -= 1
    num1, num2 = map(int, input().split())

    for i in range(1, num1 + 1):
        answer *= num2
        num2 -= 1
        answer //= i
    
    print(answer)