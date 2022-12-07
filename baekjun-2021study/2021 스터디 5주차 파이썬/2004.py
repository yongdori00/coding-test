import sys
input = sys.stdin.readline

def gcd(num1, num2):
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num2

num1, num2 = map(int, input().split())
answer = 1
k_mul = 1
N_two = 0
N_five = 0

if num1 - num2 < num2:
    num2 = num1 - num2

for t_num2 in range(num2, 0, -1):
    k_mul *= t_num2
    answer *= num1

    gcd_k = gcd(k_mul, answer)
    
    answer //= gcd_k
    k_mul //= gcd_k

    while answer % 2 == 0:
        N_two += 1
        answer //= 2
    while answer % 5 == 0:
        N_five += 1
        answer //= 5

    num1 -= 1

if(N_two >= N_five):
    answer = N_five
else:
    answer = N_two

print(answer)
