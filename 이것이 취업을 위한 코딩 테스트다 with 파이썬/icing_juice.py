import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rec(i, j):
    global ice_map, visited

    visited[i][j] = True

    if i + dy[0] < n and ice_map[i + dy[0]][j + dx[0]] == 0 and visited[i + dy[0]][j + dx[0]] == False:
        rec(i + dy[0], j + dx[0])
    if j + dx[1] < m and ice_map[i + dy[1]][j + dx[1]] == 0 and visited[i + dy[1]][j + dx[1]] == False:
        rec(i + dy[1], j + dx[1])
    if i + dy[2] >= 0 and ice_map[i + dy[2]][j + dx[2]] == 0 and visited[i + dy[2]][j + dx[2]] == False:
        rec(i + dy[2], j + dx[2])
    if j + dx[3] >= 0 and ice_map[i + dy[3]][j + dx[3]] == 0 and visited[i + dy[3]][j + dx[3]] == False:
        rec(i + dy[3], j + dx[3])

visited = []
ice_map = []

answer = 0

n, m = map(int, input().strip().split())

visited = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    ice_map.append(list(map(int,input().strip())))

for i in range(n):
    for j in range(m):
        if ice_map[i][j] == 0 and visited[i][j] == False:
            rec(i, j)
            answer += 1

print(answer)