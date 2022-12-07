n = int(input())

list_arr = []
dis = []

for i in range(n):
    arr = list(map(int, input().split()))
    list_arr.append(arr)
    arr = [0 for j in range(3)]
    dis.append(arr)

for i in range(n):
    if i == 0:
        dis[i][0] = 0 + list_arr[i][0]
        dis[i][1] = 0 + list_arr[i][1]
        dis[i][2] = 0 + list_arr[i][2]
    else:
        dis[i][0] = min(dis[i - 1][1], dis[i - 1][2]) + list_arr[i][0]
        dis[i][1] = min(dis[i - 1][0], dis[i - 1][2]) + list_arr[i][1]
        dis[i][2] = min(dis[i - 1][0], dis[i - 1][1]) + list_arr[i][2]

print(min(min(dis[n - 1][0], dis[n - 1][1]), dis[n -1][2]))