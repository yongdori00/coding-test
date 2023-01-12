import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = []
dx_list = [10001 for i in range(M + 1)]
dx_list[0] = 0

for i in range(N):
    num_list.append(int(input()))

for i in num_list:
    for j in range(M + 1):
        if j - i < 0:
            continue

        if dx_list[j - i] == 0:
            dx_list[j] = 1
        else:
            dx_list[j] = min(dx_list[j], dx_list[j-i] + 1)

if dx_list[M] == 10001:
    dx_list[M] = -1
print(dx_list[M])