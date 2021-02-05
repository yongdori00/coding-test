n = int(input(""))
n_list = []
n_mode = [0 for i in range(8001)]
cnt = 0
modeNum = 0
num = 0
sum = 0
median = 0
median_cnt = 0

for i in range(0, n):
    n_list.append(int(input("")))
    sum += n_list[i]
    n_mode[n_list[i] + 4000] += 1

for i in range(0, 8001):
    if n_mode[i] > num :
        num = n_mode[i]
        modeNum = i - 4000

for i in range(0, 8001):
    if n_mode[i] == num:
        cnt += 1
    if cnt == 2:
        modeNum = i - 4000
        break

mean = sum / n
if(mean - sum // n >= 0.5):
    mean = sum // n + 1
else:
    mean = sum // n

for i in range(0, 8001):
    while n_mode[i] != 0:
        median_cnt += 1
        n_mode[i] -= 1
    if median_cnt >= (n / 2):
        median = i - 4000
        break

print(mean)
print(median)
print(modeNum)
print(max(n_list) - min(n_list))