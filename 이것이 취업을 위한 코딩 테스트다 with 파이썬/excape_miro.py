import sys

input = sys.stdin.readline

mapp = []

n, m = map(int, input().strip().split())

visited = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    mapp.append(list(map(int, input().strip())))

def dfs(length, i, j):
    global answer, visited

    if i == n - 1 and j == m - 1 and answer > length:
        answer = length
        return

    print(length)

    if i + 1 < n and mapp[i+1][j] == 1 and visited[i+1][j] == False:
        visited[i+1][j]
        dfs(length + 1, i + 1, j)
    if j + 1 < m and mapp[i][j+1] == 1:
        dfs(length + 1, i, j + 1)
    if i - 1 >= 0 and mapp[i-1][j] == 1:
        dfs(length + 1, i - 1, j)
    if j - 1 >= 0 and mapp[i][j-1] == 1:
        dfs(length + 1, i, j - 1)

length = 0
answer = 1000000
visited[0][0] = True
dfs(length, 0, 0)

print(answer)