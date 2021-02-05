n = int(input())

arr = [0 for i in range(n + 4)]
Max = [0 for i in range(n + 4)]
answer = 0

for i in range (3, n + 3):
    arr[i] = int(input())

#Max[1] = arr[1]
#if n >= 2:
#    Max[2] = Max[1] + arr[2]
#if n >= 3:
 #   Max[3] = max(Max[1], arr[0]) + arr[2]

for i in range(3, n + 3):
    Max[i] = max(Max[i - 3] + arr[i - 1], Max[i - 2]) + arr[i]
    Max[i] = max(Max[i - 1], Max[i])
    answer = max(answer, Max[i])

print(answer)