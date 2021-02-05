def dfs(cnt):
    if cnt == n:
        for i in range (n):
            print(num_list[i], end = " ")
        print()
        return
    
    for i in range (1, num + 1):
        if visited[i] == False:
            visited[i] = True
            num_list[cnt] = i
            if cnt == 0:
                dfs(cnt + 1)
            elif num_list[cnt - 1] < num_list[cnt]:
                dfs(cnt + 1)
            visited[i] = False

num, n = input().split()

num = int(num)
n = int(n)

num_list = [0 for i in range (n + 1)]
visited = [False for i in range (num + 1)]

dfs(0)