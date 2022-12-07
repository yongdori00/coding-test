def gcd(num1, num2):
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num2

num1, num2 = map(int, input().split())

answer = 1
k_mul = 1

for i in range(num2, 0, -1):
    k_mul *= i
    answer *= num1

    gcd_k = gcd(k_mul, answer)
    
    answer //= gcd_k
    k_mul //= gcd_k

    answer %= 10007
    num1 -= 1

print(answer)