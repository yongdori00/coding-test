n = int(input())

d = [0] * 1000

d[0], d[1] = 1, 3

for i in range(2, n):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n]) 