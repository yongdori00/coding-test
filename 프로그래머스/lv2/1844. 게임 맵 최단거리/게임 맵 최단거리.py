from collections import deque

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def solution(maps):
    answer = 0
    x, y = 0, 0
    
    sum_map = [[100000 for i in range(len(maps[0]))] for i in range(len(maps))]
    queue = deque()
    
    queue.append([x, y])
    sum_map[x][y] = 1
    
    while queue:
        list_ = queue.popleft()
        x, y = list_[0], list_[1]
            
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 > ddx or ddx >= len(maps[0]) or 0 > ddy or ddy >= len(maps):
                continue
            if maps[ddy][ddx] != 0 and sum_map[y][x] + 1 < sum_map[ddy][ddx]:
                queue.append([ddx, ddy])
                sum_map[ddy][ddx] = sum_map[y][x] + 1
        
        print(x, y)
    
    print(sum_map)
    
    if sum_map[len(sum_map) - 1][len(sum_map[0]) - 1] == 100000:
        answer = -1
    else:
        answer = sum_map[len(sum_map) - 1][len(sum_map[0]) - 1]
    return answer