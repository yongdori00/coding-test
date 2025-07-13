from collections import deque

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def solution(maps):
    answer = 0
    x, y = 0, 0
    
    #각 위치에 대한 합계
    sum_map = [[100000 for i in range(len(maps[0]))] for i in range(len(maps))]
    queue = deque()
    
    #시작 위치에 대해서
    queue.append([x, y])
    sum_map[x][y] = 1
    
    #queue로 풀이
    while queue:
        list_ = queue.popleft()
        x, y = list_[0], list_[1]
            
        #상하좌우에 대해서 queue 삽입
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            #map을 벗어나는 경우는 스킵
            if 0 > ddx or ddx >= len(maps[0]) or 0 > ddy or ddy >= len(maps):
                continue
            #벽이 아니면서 sum_map[ddy][ddx]의 값이 현재 + 1보다 크면 업데이트
            if maps[ddy][ddx] != 0 and sum_map[y][x] + 1 < sum_map[ddy][ddx]:
                queue.append([ddx, ddy])
                sum_map[ddy][ddx] = sum_map[y][x] + 1
    
    #목적지에 도달 여부
    if sum_map[len(sum_map) - 1][len(sum_map[0]) - 1] == 100000:
        answer = -1
    else:
        answer = sum_map[len(sum_map) - 1][len(sum_map[0]) - 1]
    return answer