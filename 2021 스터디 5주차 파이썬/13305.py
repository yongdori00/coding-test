n = int(input())

distance = list(map(int, input().split()))
weight = list(map(int, input().split()))

minW = weight[0]
answer = 0

for i in range (len(distance)):
    if minW > weight[i]:
        minW = weight[i]
    answer += minW * distance[i]

print(answer)