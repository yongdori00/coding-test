n = int(input())

num = 9

for i in range(1, n):
    num = (num * 2 - i) % 1000000000

print(num)