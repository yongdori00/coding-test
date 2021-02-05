n = int(input())
arr = []
answer = 0

arr = list(map(int, input().split()))

arr.sort()

for i in range(n):
    for j in range(0, i + 1):
        answer += arr[j]

print(answer)