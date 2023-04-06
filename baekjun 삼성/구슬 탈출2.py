import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def move(dir, r_index, b_index):
    if dir == 0:
        if r_index[0] == b_index[0]:
            if r_index[1] > b_index[1]:
            else:


    elif dir == 1:
        if r_index[1] == b_index[1]:
            if r_index[0] > b_index[0]:
            else:

    elif dir == 2:
        if r_index[0] == b_index[0]:
            if r_index[1] < b_index[1]:
            else:

    elif dir == 3:
        if r_index[0] == b_index[0]:
            if r_index[1] < b_index[1]:
            else:

    while

def bfs():


input = sys.stdin.readline

N, M = map(int, input().split())
board = list()

b_index = []
r_index = []

for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'B':
            b_index = [i, j]
        if board[i][j] == 'R':
            r_index = [j, j]

