import sys

input = sys.stdin.readline

N, k = map(int, input().split())

list1 = list(map(int, input().rstrip().split()))
list2 = list(map(int, input().rstrip().split()))

list1.sort()
list2.sort(reverse=True)

for i in range(k):
    if list1[i] < list2[i]:
        list1[i] = list2[i]
    else:
        break

answer = sum(list1)

print(answer)