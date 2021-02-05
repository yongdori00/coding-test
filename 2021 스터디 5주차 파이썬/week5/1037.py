n = int(input())
arr = list(map(int, input().split()))

answer = 0

arr.sort()

if n % 2 == 1:
    answer = arr[n // 2] * arr[n // 2]
else:
    answer = arr[0] * arr[n - 1]

print(answer)
