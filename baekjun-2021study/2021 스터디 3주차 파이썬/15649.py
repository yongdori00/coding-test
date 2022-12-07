def dfs (cnt):
    if cnt == n:
        for i in range(0, n):
            print(list_num[i], end = " ")
        print()
        return
    
    for i in range(1, num + 1):
        if list_visited[i] == False:
            list_visited[i] = True
            list_num[cnt] = i
            dfs(cnt + 1)
            list_visited[i] = False 

num, n = (input("")).split()

num = int(num)
n = int(n)

list_num = [0 for i in range (n + 1)]
list_visited = [False for i in range (num + 1)]

dfs(0)