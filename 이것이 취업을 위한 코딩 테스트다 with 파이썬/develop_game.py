import sys
input = sys.stdin.readline

answer = 1
spin_num = 0
mapp = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().strip().split())
x, y, direction = map(int, input().strip().split())

for i in range(n):
    mapp.append(list(map(int, input().strip().split())))

visited = [[False for i in range(m)] for j in range(n)]

mapp[y][x] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:

    turn_left()

    temp_x = x + dx[direction]
    temp_y = y + dy[direction]

    #한번도 만나지 않은 육지
    if mapp[temp_x][temp_y] == 0 and visited[temp_x][temp_y] == False:
        answer += 1
        x = temp_x
        y = temp_y
        visited[temp_x][temp_y] = True
        spin_num = 0
        continue
    #막혀있는 길
    else:
        spin_num += 1

    #다 돌았으면서 뒤가 육지
    if spin_num == 4 and mapp[x - dx[direction]][y - dy[direction]] == 0:
        x = x - dx[direction]
        y = y - dy[direction]
        spin_num = 0
        continue

    #다 돌았으면서 뒤가 바다
    elif spin_num == 4 and mapp[x - dx[direction]][y - dy[direction]] == 1:
        print(answer)
        break


