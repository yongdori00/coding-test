import sys

n = int(input())

arr = []
answer = 0

for i in range(n):
    k = int(sys.stdin.readline())
    if(k != 0):
        arr.append(k)
    else:
        if len(arr) == 0:
            continue
        else:
            arr.pop()

for i in range(len(arr)):
    answer += arr[i]

print(answer)
    