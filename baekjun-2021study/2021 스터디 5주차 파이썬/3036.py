def gcd(num1, num2):
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num2

n = int(input())
arr = list(map(int, input().split()))

gcd_num = [0 for i in range(len(arr))]

for i in range(1, len(arr)):
    gcd_num[i] = gcd(arr[0], arr[i])

for i in range(1, len(arr)):
    mom = arr[0] // gcd_num[i]
    son = arr[i] // gcd_num[i]

    print(str(mom) + '/' + str(son))