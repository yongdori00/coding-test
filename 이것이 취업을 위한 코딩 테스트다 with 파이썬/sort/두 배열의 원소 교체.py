import sys

input = sys.stdin.readline

N, k = map(int, input().split())

list1 = list(map(int, input().rstrip().split()))
list2 = list(map(int, input().rstrip().split()))

#1반 리스트는 작은 것부터 정렬, 2번 리스트는 큰 것 부터 정렬 
list1.sort()
list2.sort(reverse=True)

#1번의 작은 것부터 <-> 2번의 큰 것부터 바꿔야 1번 리스트의 합이 커짐.
for i in range(k):
    if list1[i] < list2[i]:
        list1[i] = list2[i]
    else:
        break

answer = sum(list1)

print(answer)