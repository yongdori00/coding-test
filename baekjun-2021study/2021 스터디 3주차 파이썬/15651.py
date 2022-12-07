def dfs(cnt):
    if cnt == n:
        for i in range(n):
            print(num_list[i], end = " ")
        print()

    if cnt > n:
        return

    for i in range(1, num + 1):
        num_list[cnt] = i
        dfs(cnt + 1)

num, n = input().split()

num = int(num)
n = int(n)

num_list = [0 for i in range (n + 1)]
visited = [False for i in range(num + 1)]

dfs(0)