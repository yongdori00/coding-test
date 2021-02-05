n = int(input())

arr = []
dis = []

for i in range(0, n):
    i_list = list(map(int, input().split()))
    arr.append(i_list)
    i_list = [0 for j in range(0, i + 1)]
    dis.append(i_list)

answer = 0


    
for i in range(0, n):
    for j in range(0, i + 1):
        if j == 0:
            if i == j == 0:
                dis[i][j] = 0 + arr[i][j]
            else:
                dis[i][j] = dis[i - 1][j] + arr[i][j]
        elif j == i:
            dis[i][j] = dis[i - 1][j - 1] + arr[i][j]
        else:
            dis[i][j] = max(dis[i - 1][j], dis[i - 1][j - 1]) + arr[i][j]

for i in range(0, n):
    answer = max(dis[n - 1][i], answer)

print(answer)