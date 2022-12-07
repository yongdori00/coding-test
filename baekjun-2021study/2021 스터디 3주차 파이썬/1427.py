n = (int(input("")))
n_len = 0
tempn = n

while tempn > 0:
    n_len += 1
    tempn = tempn // 10

n_list = [0 for i in range(0, n_len)]

for i in range(0, n_len):
    n_list[n_len - i - 1] = (int)(n % 10)
    n = n // 10

n_list.sort(reverse=True)
for i in range(0, n_len):
    print(n_list[i], end='')
