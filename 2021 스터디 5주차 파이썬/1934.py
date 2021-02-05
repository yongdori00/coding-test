n = int(input())
num1 = 0
num2 = 0
gcd = 1

while n > 0:
    num1, num2 = map(int, input().split())
    t_num1 = num1
    t_num2 = num2

    while t_num1 % t_num2 != 0:
        temp = t_num1
        t_num1 = t_num2 % t_num1
        t_num2 = temp
    gcd = t_num2
    answer = num1 // gcd * num2

    print(answer)

    n-=1